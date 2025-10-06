import math

V = int(input("Введите объём шара "))
r = ((V * 3) / (4 * math.pi)) ** (1 / 3)

print("Радиус этого шара = ", r)
