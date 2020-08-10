""" реализация 9_го задания  помощью сторонней бибилиотеки Yattag """
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('p', id='main'):
            text('some text in main paragrath!')
        with tag('a', href='/my-url'):
            text('link to url of your')

result = doc.getvalue()

"Реализация без сторонних библиотек"


# parent
class Tag(object):
    def show(self):
        pass


# image tag
class Image(Tag):
    def show(self):
        print('<img></img>')

    def shatr(self):
        print('<img src=""></img>')


# text paragraph
class Text(Tag):
    def show(self):
        print('<p></p>')

    def shatr(self):
        print('<p align=""></p>')


# link
class Link(Tag):
    def show(self):
        print('<a></a>')

    def shatr(self):
        print('<a href=""></a>')


# input field
class Input(Tag):
    def show(self):
        print('<input></input>')

    def shatr(self):
        print('<input value=""></input>')


class CreateTag:
    def gethtml(self, type_):
        if type_ == 'image' or type_ == 'src':
            return Image()
        elif type_ == 'input' or type_ == 'val':
            return Input()
        elif type_ == 'text' or type_ == 'al':
            return Text()
        elif type_ == 'link' or type_ == 'href':
            return Link()


html = CreateTag()
html.gethtml('src').shatr()
html.gethtml('input').show()
html.gethtml('al').shatr()
html.gethtml('link').show()
html.gethtml('href').shatr()
