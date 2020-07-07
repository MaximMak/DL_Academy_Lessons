__author__ = 'Makarkin Maxim Boricovich'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
age = int(input("Please input your age: "))
if age <= 0:
    print("You are entering the wrong age. It cannot be less than 1.")
else:
    name = input("Please input you name: ")
    age = age - 18
    if age == 0:
        print(f'{name} your age is 18 years old')
    elif -18 < age <= 0:
        print(f'{name} on {-age} year/s less then 18')
    else:
        print(f'{name} on {age} year/s more then 18')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
variable1 = input("Please input variable1: ")
variable2 = input("Please input variable2: ")
print("variables", variable1, variable2)
tmp = variable1
variable1 = variable2
variable2 = tmp
print("Change variables", variable1, variable2)
# Or may this happens with this solution variable1,variable2 == variable2,variable1

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
print("Lets find out the value of quadratic equation ax^2 + bx + c = 0:")
a = float(input("Input your coefficients a = "))
b = float(input("Input your coefficients b = "))
c = float(input("Input your coefficients c = "))
import math

disc = b ** 2 - 4 * a * c

if disc > 0:
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)
    print("positive value", root1, "negative value", root2)
elif disc == 0:
    root0 = -b / (2 * a)
    print("If discriminant equal 0", root0)
else:
    print("There`s no roots for negative value of the discriminant!")
