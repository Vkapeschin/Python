# Задача 1. Сумма цифр числа.

# n = int(input('Input a number: '))
# summ = 0
# while n > 0:
#     x = n % 10
#     summ = summ + x
#     n = n // 10
# print(summ)

# Задача 2. Делитель числа.

# a = int(input('Input a number: '))
# flag = True
# i = 2
# while flag:
#     if a % i == 0:
#         flag = False
#     elif i > a:
#         flag = False
#     else: i += 1
# print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# Про вагоны

# i = int(input())
# j = int(input())

# if i == j:
#     print('Недостаточно информации')
# else:
#     print(f'{i+j-1}')

#7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
# год является високосным, если его номер кратен 4, но не кратен 100, 
# или он кратен 400.**Input:**2016**Output:**YES

# year = int(input('Input a year: '))
# print(f'{year % 4 == 0 and year % 100 != 0 or year % 400 == 0}')

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 0,34 -> 3

# num = float(input())
# print(f'{int((num * 10) % 10)}')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# x1 = float(input('input x1'))
# y1 = float(input('input y1'))
# x2 = float(input('input x2'))
# y2 = float(input('input y2'))

# (x2-x1)*(x2-x1)

# x1 = float(input("введите x1: "))
# x2 = float(input("введите x2: "))
# y1 = float(input("введите y1: "))
# y2 = float(input("введите y2: "))


# print(((x1-x2)**2 +(y1-y2)**2)**0.5)