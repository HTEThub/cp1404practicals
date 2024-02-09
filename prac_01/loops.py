#eg
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 1-1, -1):
    print(i, end=' ')
print()

#c
num = int(input("Input Number(s):"))
for i in range(num):
    print("*", end=' ')
print()

#d
num = int(input("Input Number(s):"))
for i in range(1, num+1):
    print("*" * i)
