# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a = [1, 2, 4, 0]
b = []
for i in a:
    i = i**2
    b.append[i]
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
a = ['Банан', 'дыня', 'r', 4, 'ee', 'ee']
b = [4, 'дыня', 'ee', 3, 'Банан']
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst_generator = [i for i in range(-100, 100) if i > 0 and i % 3 == 0 and i % 4 != 0]
print(lst_generator)
