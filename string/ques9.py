s1 = "PYnative29@#8496"
total = 0
count = 0
for char in s1:
    if char.isdigit():
        total += int(char)
        count +=1
avg = total / count     
print("sum is:", total, "avg is:", avg)   