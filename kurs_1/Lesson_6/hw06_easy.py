import os, shutil, sys


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


def mkdir(dirname):
    path = os.path.join(os.getcwd(), dirname)
    try:
        os.mkdir(path)
        print(f'Папка {dirname} создана')
    except FileExistsError:
        print(f'Папка {dirname} уже существует')

def rm(dirname):
    path = os.path.join(os.getcwd(), dirname)
    try:
        os.rmdir(path)
        if not os.path.isdir(path):
            print(f'Папка {dirname} успешно удалена.')
    except FileNotFoundError:
        print(f'Папка {dirname} не найдена.')


# Задача-3:
# Напишите скрипт отображающий папки текущей директории.

def lsdir(path):
    list_dir = [dir for dir in os.listdir(path) if os.path.isdir(dir)]
    list_dir.sort()
    print(*list_dir)

ls_path = os.getcwd()
lsdir(ls_path)


list = os.listdir()
for i in list:
    print(i)


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copyfile(filename):
    newfile = filename + '.copy'
    shutil.copy(filename, newfile)
    if os.path.isfile(newfile):
        print('Копия файла создана')


copyfile(__file__)
