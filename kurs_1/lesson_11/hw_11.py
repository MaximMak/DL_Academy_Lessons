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