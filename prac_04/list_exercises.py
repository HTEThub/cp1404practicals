# NUM_FILE = "numbers"
# input_times = 5
# numbers = []
# total = 0
#
# for eachInput in range(input_times):
#     number = int(input("Enter any number: "))
#     numbers.append(number)
#     total += number
#
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
#
# average_num = total / input_times
# print(f"The average of the numbers is {average_num}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")
while username != "quit":
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")
    username = input("Enter your username: ")
