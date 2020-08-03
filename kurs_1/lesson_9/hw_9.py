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


class