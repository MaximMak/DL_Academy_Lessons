# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
n = int(input('Input element n: '))
m = int(input('Input element m: '))


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(n, m + 1):
    print(fibonacci(i))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

sort_to_max = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
temp = 0
for index in range(len(sort_to_max)):
    for i in range(len(sort_to_max) - 1):
        if sort_to_max[i] > sort_to_max[i + 1]:
            temp = sort_to_max[i]
            sort_to_max[i] = sort_to_max[i + 1]
            sort_to_max[i + 1] = temp
print(sort_to_max)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def numbs(x):
    if '0' <= x <= '9':
        return 1
    else:
        return 0


s = "5a 3 k 99 d00"
for i in filter(numbs, s):
    print(i)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# a = [x1, y1, x2, y2, x3, y3, x4, y4]
# if (y1 = y4) and (y2=y3) and (abs(x1-x2)=abs(x3-x4)) then
# write('Точки являются вершинами параллелограмма')
# else
# write('Точки не являются вершинами параллелограмма');