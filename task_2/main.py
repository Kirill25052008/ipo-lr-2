k = int(input("Введите кол-во яблок "))
n = int(input("Введите кол-во школьников "))

count_of_apples = k//n
count_of_apples_in_busket = k%n

print("кол-во яблок у школьников = ", count_of_apples)
print("кол-во яблок в корзине = ", count_of_apples_in_busket)
