import os
import shutil
import sys


# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))

except:
    print("Already exist")
a = input("enter something ")
print(a)

try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")

# Задача-3:
# Напишите скрипт отображающий папки текущей директории.
list = os.listdir()
for i in list:
    print(i)


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)


first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file, backup_file)
