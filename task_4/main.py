import math

x = int(input("Введите значение переменной x"))
y = int(input("Введите значение переменной y"))

z = abs((x ** (y / x)) - math.sqrt((y / x) ** (1 / 3))) + (y - x)

print(z)
