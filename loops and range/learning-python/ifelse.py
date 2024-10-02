
a = int(input("enter the percentage:"))
if a >= 70:
    print("distinction")
elif a > 60 and a <= 69:
    print("merit")
elif a > 40 and a <= 60:
    print("pass")
else:
    print("fail")

t = int(input("enter percentage mark"))
if t >= 80:
    print("A")
elif t >= 70 and t <= 79:
    print("B")
elif t >= 60 and t <= 69:
    print("C")
elif t >=50 and t <= 59:
    print("D")
elif t >= 40 and t <= 49:
    print("E")
else:
    print("F")
    