tup1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tup1 = tuple(sorted(list(tup1), key=lambda x: x[1]))
print(tup1)
