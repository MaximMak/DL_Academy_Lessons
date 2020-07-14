__author__ = 'Makarkin Maxim Boricovich'
import math
# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

age = int(input('Please input your age: '))
if age <= 0:
    print("You are entering the wrong age. It cannot be less than 0.")
elif 0 < age < 18:
    print("Извините, пользоваться данным ресурсом можно только с 18 лет")
else:
    name = input("Доступ разрешен")

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...


while True:
    input_data = input('Выберите четные или не четные числа вывести на экран: 1 для четных, 2 для не четных')
    if not input_data.isnumeric():
        print("Вы ввели не число. Попробуйте снова: ")
    elif not 0 < int(input_data) <= 2:
        print("Ваше число не диапазоне. Попробуйте снова")
    else:
        print("Число в правильном диапазоне.")
        break
input_data = int(input_data)
if input_data == 1:
    for i in range(21):
       if int(i) % 2 == 0 and i != 0:
          print(i, end=' ')
elif input_data == 2:
    for i in range(20):
       if int(i) % 2 != 0 and i != 0:
          print(i, end=' ')
# Second way:
while True:
    input_data = input('Четные или Нечетные?')
    if not input_data == input_data.lower() in ['четные', 'Четные', 'нечетные', 'Нечетные']:
        print('Я не понимаю, что вы от меня хотите... Попробуйте снова: ')
    else:
        print(f'Ура! ты выбрал {input_data}')
        break
if input_data.lower() in ['четные', 'Четные']:
    for i in range(21):
        if int(i) % 2 == 0 and i != 0:
            print(i, end=' ')
elif input_data.lower() in ['нечетные', 'Нечетные']:
    for i in range(20):
        if int(i) % 2 != 0 and i != 0:
            print(i, end=' ')
else:
    print('Я не понимаю, что вы от меня хотите...')
# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Через встроенную функцию max.
x = input('Введите произвольное целое число: ')
list_of_digits = list(map(int, str(x)))
print("Максимальная цифра во введенном числе : ", max(list_of_digits))

# Через while.
a = int(input())
m = a%10
if m == 9:
    print(m)
else:
    a = a//10
    while a > 0:
        if a % 10 > m:
            m = a % 10
        a = a // 10
    print(m)

# Через for
lst = int(input())
lst = list(map(int, str(lst)))
max = lst[0]
for i in lst:
    if i > max:
        max = i
print(max)