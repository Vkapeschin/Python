# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

# import random

# lst = []
# n = int(input('Введите размер списка: '))
# x = int(input('Введите значение: '))

# for i in range(n):
#     lst.insert(i, random.randint(1, 5))
# print(lst)

# count = 0
# for i in range(len(lst)):
#     if x == lst[i]:
#         count += 1

# print(count)



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

# import random

# lst = []
# n = int(input('Введите размер списка: '))
# x = int(input("Введите значение: "))

# for i in range(n):
#     lst.insert(i, random.randint(1, 100))
# print(lst)

# a = (lst[0])
# for i in range(len(lst)):
#     if abs(lst[i] - x) < abs(a - x):
#         a = lst[i]
# print(a)


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

word = list(input('Введите слово заглавными буквами: '))
newword = word
count = 0

for i in range(len(word)):
    if word[i] == 'A' or 'E' or 'I' or 'O' or 'U' or 'L' or 'N' or 'S' or 'T' or 'R':
        count += 1
        print('true')
    elif word[i] == 'D' or 'G':
        count += 2
    elif word[i] == 'B' or 'C' or 'M' or 'P':
        count += 3
    elif word[i] == 'F' or 'H' or 'V' or 'W' or 'Y':
        count += 4
    elif word[i] == 'K':
        count += 5
    elif word[i] == 'J' or 'X':
        count += 8
    elif word[i] == 'Q' or 'Z':
        count += 10 
    else:
        print('Пишите по-английски')
print(count)