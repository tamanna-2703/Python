def check(t):
    return all(i == t[0] for i in t)

tup1 = (45, 45, 45, 45)
print(check(tup1))