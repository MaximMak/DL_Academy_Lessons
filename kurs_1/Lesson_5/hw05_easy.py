# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    i = i**2
    print(i)
    

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

list_1 = ['apple', 'orange', 'cucumber', 'potato']
List_2 = ['apple', 'orange', ]
union_list = list(set(list_1) & set(List_2))
print(union_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a = [7, 2, 13, 44, 5]
b = []
for i in a:
    i = i**2
    b.append(i)
print(b)
lst_generator = [i for i in range(-100, 100) if i > 0 and i % 3 == 0 and i % 4 != 0]
print(lst_generator)

