def string(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag

s1 = "Yn"
s2 = "PYnative"
flag = string(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "ynf"
s2 = "PYnative"
flag = string(s1, s2)
print("s1 and s2 are balanced:", flag)





