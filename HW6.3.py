num = int(input("Введіть число: "))

while num > 9:
    a = 1
    for i in str(num):
        a *= int(i)
    num = a

print(num)
