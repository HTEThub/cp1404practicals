# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove?: ")
#
#
# while name_to_remove not in names:
#      print("The name is not in the list.")
#      name_to_remove = input("Who do you want to remove?: ")
#
#
# if name_to_remove in names:
#     print(f"You removed {name_to_remove}")
#     names.remove(name_to_remove)
#     print(", ".join(names))
# else:
#     print("The name is not in the list.")

# things = [True, 1.2, "Good", [1, 10]]
# print(things[-2])
# print("%".join([things[2][1:-1]]))
# print([str(t)[0] for t in things])
# print([len(str(t)) for t in things])
# print([t for t in things if type(t) in (float, int)])
# print([t for t in things if isinstance(t, int)])

# 1. numbers?
# 2.
# 3. age
# 4. coordinates
# 5. mutant_or_not
# 6.

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# for eachElement in range(len(data)):
#     element = data[eachElement]
#     for eachElement2 in range(len(element)):
#         print(element[eachElement2])

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)
