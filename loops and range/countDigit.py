a = int(input("enter digit:"))
counter = 0
if a < 0:
    a = -1 * a
if a == 0:
    print(1)
while a != 0:
    a = a//10
    counter += 1
    print(counter)