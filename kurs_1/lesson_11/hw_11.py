'''
«Есть два писателя, которые по очереди в течении определенного времени (у каждого разное)
пишут в одну книгу. Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя),
 которые ждут не дождутся, чтобы прочитать новые записи из неё. Каждый читатель и писатель –
 отдельный поток. Одновременно книгу может читать несколько читателей, но писать единовременно
 может только один писатель.»
'''


import threading
import time

lock = threading.Lock()
wrote_event = threading.Event()
strings_count = 0


def writing(name, speed):
    """Функция написания. Принимает имя писателя и его скорость письма"""
    global strings_count  # Будем работать с глобальной переменной, так писателя пишут одну книгу фиксированной длины
    while strings_count < 3:  # Фиксируем длину книги количеством строк
        with lock:  # Блокируем ресурс, чтобы пока писатель пишет, второй не имел доступа к книге
            with open('book.txt', 'a') as book:
                print(f'{name} начал писать...')
                time.sleep(speed)  # Имитируем скорость письма автора соответствующей паузой
                book.write(f'Строка {strings_count + 1}\n')  # Записываем строку в файл книги
                print(f'{name} написал: Строка {strings_count + 1}')  # Вывод в интерпретатор для наглядности
                strings_count += 1  # Сообщаем глобальной переменной, что длинна книги увеличилась на одну строку
            wrote_event.set()  # Сообщаем читателю, что ещё одна запись сделана - можно читать
            time.sleep(1)  # Ждём, чтобы дать возможность второму потоку писателя захватить управление (для очерёдности)


def reading(reader_num):
    """Функция чтения. Принимает в качестве агрумента номер читателя."""
    while True:  # Читатель постоянно ждёт...
        wrote_event.wait()  # ...сигнала от писателя, что появилась новая запись и можно читать
        with open('book.txt', 'r') as book:
            for line in book:  # Перебирает все строки книги
                last_line = line  # И находит последнюю
            print(f'Читатель {reader_num} прочитал: {last_line[:-1]}')  # "Читает" последнюю строку
            wrote_event.clear()  # Переходит в режим ожидания следующего сигнала от писателя


# Объявление потоков для писателей, старт и присоединение к основному потоку
writer1 = threading.Thread(target=writing, args=('Гоголь', 4))
writer2 = threading.Thread(target=writing, args=('Пушкин', 2))

# Читатели - демоны, так как всегда находятся в режиме ожидания. Их нужно убить, когда писатели закончат писать.
reader1 = threading.Thread(target=reading, daemon=True, args=('1',))
reader2 = threading.Thread(target=reading, daemon=True, args=('2',))
reader3 = threading.Thread(target=reading, daemon=True, args=('3',))

writer1.start()
writer2.start()

reader1.start()
reader2.start()
reader3.start()

writer1.join()
writer2.join()


"""
Пять безмолвных философов сидят вокруг круглого стола, перед каждым философом стоит 
тарелка спагетти. Вилки лежат на столе между каждой парой ближайших философов. 
Каждый философ может либо есть, либо размышлять. Прием пищи не ограничен количеством 
оставшихся спагетти — подразумевается бесконечный запас. Тем не менее, философ может 
есть только тогда, когда держит две вилки — взятую справа и слева (альтернативная 
формулировка проблемы подразумевает миски с рисом и палочки для еды вместо тарелок 
со спагетти и вилок). Каждый философ может взять ближайшую вилку (если она доступна) 
или положить — если он уже держит её. Взятие каждой вилки и возвращение её на стол 
являются раздельными действиями, которые должны выполняться одно за другим. Вопрос 
задачи заключается в том, чтобы разработать модель поведения (параллельный алгоритм), 
при котором ни один из философов не будет голодать, то есть будет вечно чередовать 
приём пищи и размышления.»
"""

class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False

# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):
            time.sleep(0.5)
            print(f'Philosopher at {threading.currentThread()} is eating.')

# The chopsticks
N_FORKS = 5
forks = [threading.Lock() for n in range(N_FORKS)]

# Create all of the philosophers
phils = [threading.Thread(
    target=philosopher,
    args=(forks[n], forks[(n + 1) % N_FORKS])
) for n in range(N_FORKS)]

# Run all of the philosophers
for p in phils:
    p.start()




""" реализация 9_го задания  помощью сторонней бибилиотеки Yattag """
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            text('some text in main paragrath!')
        with tag('a', href='/my-url'):
            text('link to url of your')

result = doc.getvalue()
class Store:
    """Инициализируем класс магазин, с атрибутами Имя продавца, и категорией продуктов"""
    def __init__(self, seller, category, selling_plan):
        self.seller = seller
        self.category = category
        self.selling_plan = selling_plan

class Product(Store):
    def __init__(self, unique_id, product_name, price, amount):
        self.id = unique_id
        self.name = product_name
        self.price = price
        self.amount = amount

class FruitProduct(Product):
    def __init__(self, country, shelf_life):
        self.country = country
        self.shelf_life = shelf_life