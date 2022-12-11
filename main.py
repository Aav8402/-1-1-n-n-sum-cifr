# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11



# num = float(input('Введите число: '))
# summa = 0
# while num != int(num):
#     num = num*10
# print(num)
# while num != 0:                                #Через float не получилось
#     ost = num % 10
#     summa +=ost
#     num = num // 10
# print(summa)


# num = input('Введите число: ')
# summa = 0
# for i in num:
#     if i.isdigit():
#         summa += int(i)
# print(summa)


# 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль
# сам список и сумму его элементов.

# number = int(input('Введите число: '))
# my_list = []
# for n in range(1, number+1):
#     my_list.append(round(((1+1/n)**n), 2))
# print(my_list)
# print(sum(my_list))



# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE
# не использовать! Реализовать свой метод
-----------------------------------------------
