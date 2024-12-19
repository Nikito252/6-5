#Написать программу, которая:

#Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
#Находит количество положительных, отрицательных и нулевых элементов в списке.
#Выводит значения и их (положительных, отрицательных и нулевых) количество вместе с процентом от общего количества.
#Выводит самое большое и самое маленькое значение
import random
#создание списка от -50 до 50
a = [ random.randint(-50,50) for i in range(25)]
print(a)
print("Минимальное значение",min(a))
print("Максимальное значение",max(a))
count_positive = 0
count_negative = 0
count_zero = 0
procent_zero = 0
for i in a:
    if i>0:
        count_positive +=1
        procent_positive = count_positive/25 * 100
    if i<0:
        count_negative +=1
        procent_negative = count_negative/25 * 100
    if i==0:
        count_zero +=1
        procent_zero = count_zero/25 * 100
print("Количество положительных элементов: ",count_positive,"Их процент составляет: ",procent_positive)
print("Количество отрицательных элементов: ",count_negative,"Их процент составляет:",procent_negative)
print("Количество нулевых элементов: ",count_zero,"Их процент составляет: ",procent_zero)
