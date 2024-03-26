# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

MENU = ("(H)ello\n"
        "(G)oodbye\n"
        "(Q)uit")
name = input("Enter your name: ")
print(MENU)
choice = str(input(">>> ")).upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Input")
    print()
    print(MENU)
    choice = str(input(">>> ")).upper()
print("Finished")
