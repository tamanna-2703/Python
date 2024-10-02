str1 = input("enter string:")
print("string: ", str1)
lower = []
upper = []
for char in str1:
    if char. islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ' '.join(lower + upper)
print("the resultant string is: ",sorted_string)
