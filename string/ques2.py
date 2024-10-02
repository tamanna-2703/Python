str1 = input("enter first string: ")
str2 = input("enter second string: ")
mid= int(len(str1)/2) #not div by 2 append at back
x = str1[:mid:]
x = x + str2
x = x + str1[mid:]
print("after appending new string in middle:", x)
