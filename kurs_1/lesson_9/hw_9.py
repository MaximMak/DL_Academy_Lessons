# """ реализация 9_го задания  помощью сторонней бибилиотеки Yattag """
# from yattag import Doc
#
# doc, tag, text = Doc().tagtext()
#
# with tag('html'):
#     with tag('body'):
#         with tag('p', id='main'):
#             text('some text in main paragrath!')
#         with tag('a', href='/my-url'):
#             text('link to url of your')
#
# result = doc.getvalue()
"""
Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов.
Разработать класс Products, продукт описывается следующими параметрами: уникальный идентификатор,
название продукта, стоимость, количество. Разрабо тать класс FruitProduct на базе класс Product,
фрукт характеризуется параметрами: страна изготовителя, срок годности.

"""

class Product:

    def __init__(self, unique_id, product_name, price, amount):
        self.id = unique_id
        self.name = product_name
        self.price = price
        self.amount = amount


class FruitProduct(Product):

    def __init__(self, unique_id, product_name, price, amount, country, shelf_life):
        super().__init__(unique_id, product_name, price, amount)
        self.country = country
        self.shelf_life = shelf_life


class Store(Product):
    """Инициализируем класс магазин, с атрибутами Имя продавца, и категорией продуктов"""
    def __init__(self, seller, category, selling_plan):
        self.seller = seller
        self.category = category
        self.selling_plan = selling_plan
        self.storage = []

    def add_product(self, id, name, price, amount, country = None, sheplf_life = None):
        if country == None:
            self.storage.append(Product(id, name, price, amount))
        else:
            self.storage.append(FruitProduct(id, name, price, amount, country, sheplf_life))




MyStore = Store("Sel","grocery", 1)
MyStore.add_product("1", "dudka", 10, 1)
MyStore.add_product("1", "dudka", 10, 1, "Russia", 10)