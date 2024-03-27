from datetime import datetime
from project import Project

DEFAULT_FILE = "projects.txt"

MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (F)ilter projects by date\n" \
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
            filter_projects(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Input")

        print("----------")
        print(MENU)
        choice = input(">>> ").upper()


""" Main Choices Functions """


def load_projects(filename, projects):
    """ Open a given file and read it into memory with converted values """
    with open(filename, 'r', newline="") as in_file:
        next(in_file)
        for eachLine in in_file:
            row = eachLine.strip().split("\t")
            project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)


def save_projects(filename, projects):
    """ Open a given file and write into it with each Project attribute in the required format """
    with open(filename, 'w', newline="") as out_file:
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                           f"{project.completion}\n")


def display_projects(projects):
    """ Sort Projects by the Percentage of Completion and Print them out """
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


def filter_projects(projects):
    """ Get user input date and compare it to sorted projects' dates and filter it out """
    filtered_projects = []

    date_input = input("Show projects that start after date (d/m/yyyy): ")
    while not date_validation(date_input):
        date_input = input("Show projects that start after date (d/m/yyyy): ")
    date = date_validation(date_input)

    sorted_projects = sorted(projects)
    for project in sorted_projects:
        if project.start_date > date:
            filtered_projects.append(project)

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """ Get user inputs for new project and add it into projects """

    proj_name = input("Enter Project Name: ").strip()
    while proj_name == "":
        print("Cannot be blank")
        proj_name = input("Enter Project Name: ").strip()

    start_date = input("Enter Start Date (dd/mm/yyyy): ").strip()
    while not date_validation(start_date):
        start_date = input("Enter Start Date (dd/mm/yyyy): ").strip()

    priority = input("Enter Priority: ").strip()
    while not priority_validation(priority):
        priority = input("Enter Priority: ").strip()

    cost_estimate = input("Enter Cost Estimate: $").strip()
    while not cost_validation(cost_estimate):
        cost_estimate = input("Enter Cost Estimate: $").strip()

    completion = input("Enter Completion: %").strip()
    while not completion_validation(completion):
        completion = input("Enter Completion: %").strip()

    new_proj = Project(proj_name, start_date, priority, cost_estimate, completion)
    projects.append(new_proj)
    # print(new_proj)
    print(f"{proj_name} has been added")


def update_project(projects):
    """ Let user choose a project from a list of projects and update on completion and priority """
    for i, project in enumerate(projects):
        print(f"{i}. {project}")

    project = choice_index_validation(projects)
    print(f"\n{project}")

    new_completion = input("Update Completion (leave blank to skip): ").strip()
    while new_completion != "":
        if completion_validation(new_completion):
            project.completion = int(new_completion)
            # print(project)  #checking
            break
        else:
            new_completion = input("Update Completion (leave blank to skip): ").strip()

    new_priority = input("Update Priority (leave blank to skip): ").strip()
    while new_priority != "":
        if completion_validation(new_priority):
            project.priority = int(new_priority)
            # print(project) #checking
            break
        else:
            new_priority = input("Update Completion (leave blank to skip): ").strip()


""" Error Checking Functions """


def date_validation(date_input):
    """ Error check the date """
    try:
        datetime_obj = datetime.strptime(date_input, '%d/%m/%Y')
        return datetime_obj.date()
    except ValueError:
        print("Incorrect date format")
        return None


def choice_index_validation(projects):
    """ Error check the choice index """
    while True:
        try:
            choice = int(input("Choose a Project to update: "))
            project = projects[choice]
            break
        except IndexError:
            print("Choose a number from the list")
        except ValueError:
            print("Has to be whole number")
    return project


def priority_validation(number):
    """ Error check the priority number (copied the code from completion validation with some changes) """
    is_int = False
    try:
        number = int(number)
        if number < 0:
            print("Cannot be less than 0")
        else:
            is_int = True
    except ValueError:
        print("Has to be whole number")
    return is_int


def cost_validation(number):
    """
    Error check validate the cost number
    (copied the code from priority validation with some changes for float)
    """
    is_float = False
    try:
        number = float(number)
        if number < 0:
            print("Cannot be less than 0")
        else:
            is_float = True
    except ValueError:
        print("Has to be a whole number or with decimals")
    return is_float


def completion_validation(number):
    """ Error check the completion number """
    is_int = False
    try:
        number = int(number)
        if number < 0:
            print("Cannot be less than 0")
        elif number > 100:
            print("Cannot be over 100")
        else:
            is_int = True
    except ValueError:
        print("Has to be whole number")
    return is_int


main()
