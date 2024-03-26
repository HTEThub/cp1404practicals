import datetime
from project import Project

DEFAULT_FILE = "projects.txt"

MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (Filter projects by date\n" \
       "- (A)dd new project\n" \
       "- (U)pdate project\n" \
       "- (Q)uit project\n"


def main():
    projects = []
    load_projects(DEFAULT_FILE, projects)
    # for project in projects:  # checking if the contents are correct
    #     print(project)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter File Name: ")
            load_projects(filename, projects)
        elif choice == "S":
            filename = input("Enter File Name: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_new_projects()
        elif choice == "U":
            update_project()
        else:
            print("Invalid Input")

        print("----------")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename, projects):
    """ Open a given file and read it into memory with converted values """
    with open(filename, 'r', newline="") as in_file:
        next(in_file)
        for eachLine in in_file:
            row = eachLine.strip().split("\t")
            project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)


def save_projects(filename, projects):
    """ Open a given file and write into it with each Project attribute in the required format"""
    with open(filename, 'w', newline="") as out_file:
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                           f"{project.completion}\n")


def display_projects(projects):
    """ Sort Projects by the Percentage of Completion and Print them out"""
    incomplete_proj = []
    completed_proj = []

    for project in projects:
        if int(project.completion) == 100:
            completed_proj.append(project)
        else:
            incomplete_proj.append(project)

    print("Incomplete Porject/s: ")
    for project in incomplete_proj:
        print("\t", project)

    print("\nCompleted Projects/s: ")
    for project in completed_proj:
        print("\t", project)


main()
