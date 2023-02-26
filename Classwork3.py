# Задача 2. Переместить на k список.
# [1, 2, 3, 4]
# [4, 1, 2, 3]

lst = [1, 2, 3, 4, 5, 6, 7]
k = int(input('Введите k: '))

for i in range(k):
    lst.insert(0, lst.pop(-1))

print(lst)