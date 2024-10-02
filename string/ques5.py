str1 = input("enter string:")
alpha = []
digit = []
symbol = []
for char in str1:
    if char.isalpha():
        alpha.append(char)
    elif char.isdigit():
        digit.append(char)
    else:
        symbol.append(char)
print("characters: ",alpha, "digits:", digit, "symbols:", symbol)
char = len(alpha)
digits = len(digit)
symbol = len(symbol)
print("characters :", char, "digits:", digits, "symbols", symbol)
