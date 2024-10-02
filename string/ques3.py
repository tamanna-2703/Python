str1 = "tamanna"
str2 = "sachdeva"
print("string: ", str1, str2)
res = str1[0].upper()
l = len(str1)
mid = int(l/2)
res = res + str1[mid]
mid = int(l/2)
res = res + str1[l-1]
print("neww string 1:", res)
res2 = str2[0].upper()
l1 = len(str2)
mid2 = int(l1/2)
res2 = res2 + str2[mid2]
mid2 = int(l1/2)
res2 = res2 + str2[l1-1]
print("new string2: ", res2)
first_char = str1[0].upper() + str2[0].upper()
middle_char = str1[mid] + str2[mid2]
last_char = str1[l-1] + str2[l1-1]
result = first_char + middle_char  + last_char
print("result of two string is:", result)