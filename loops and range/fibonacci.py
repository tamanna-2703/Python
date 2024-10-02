x = int(input("enter the number upto which you want fib series: "))
a, b = 0, 1
print("fibonacci sequence:")
for i in range(x):
    print(a, end=" ")
    c = a + b
    a = b
    b = c