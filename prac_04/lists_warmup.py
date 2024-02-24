numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
# the output is 3, the first element in the list


numbers[-1]
# the output is 2, the last element in the list


numbers[3]
# the output is 1, the 4th element in the list


numbers[:-1]
# the output is the whole list in that order, from the first element to the last <<incorrect

# Correction
# the output is actually the whole list except for the last element


numbers[3:4]
# the output is 1 and 5, from the 4th element to the 5th <<incorrect

# Correction
# the output is actually just 1, from 4th element to the (5-1)th


5 in numbers
# the output is True, it is in range of the list


7 in numbers
# the output is False, it is out of range of the list


"3" in numbers
# the output is False, it is out of range of the list.
# the list contains integers, not strings


numbers + [6, 5, 3]
# I'm not sure about this one.
# Either the first 3 elements are added with these numbers or... << this one is incorrect
# The list is extended with these new numbers. << this one is correct


# 1
numbers[0] = "10"
print(numbers)

# 2
numbers[-1] = 1
print(numbers)

# 3
print(numbers[2:7])

# 4
print(9 in numbers)
