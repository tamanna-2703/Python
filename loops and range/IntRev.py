num = int(input("enter integer: "))
rev_num = 0
print("given number", num)
while num > 0:
    reminder = num % 10
    rev_num = (rev_num * 10) + reminder
    num = num // 10
    print("reverse number", rev_num)