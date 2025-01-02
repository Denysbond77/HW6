import string

text = input("Введіть строку: ")

a = text[0]
b = text[-1]

l1 = list(string.ascii_letters)
l2 = l1[l1.index(a):l1.index(b)+1]

result = "".join(l2)

print(result)

