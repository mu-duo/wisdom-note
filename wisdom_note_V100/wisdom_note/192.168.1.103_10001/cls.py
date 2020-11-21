import json
import numpy
from conf import *

__all__ = ['Book', 'Draft']


class Book(object):
    # 初始化属性
    def __init__(self, book_name=''):
        if book_name == '':
            book_name = input('input book name: ')
        self.book_path = PATH + book_name + '/book'
        self.draft_path = PATH + book_name + '/draft'
        self.info_path = PATH + book_name + '/info.json'
        self.size = (0, 0)
        self.last_page = 1
        self.end_page = 1
        self.page = 1
        if book_name != '':
            self.open_book()

    # 获取书本参数
    def open_book(self):
        try:
            with open(self.info_path, 'r') as f:
                data = json.load(f)
                self.size = data['size']
                self.page = data['last_page']
                self.last_page = data['last_page']
                self.end_page = data['end_page']
        except FileNotFoundError:
            print('the book is not exist')
            book_name = input('input book name again:')
            self.book_path = PATH + book_name + '/book'
            self.draft_path = PATH + book_name + '/draft'
            self.info_path = PATH + book_name + '/info.json'

    # 翻页到page

    def turn_to_page(self, page):
        page = int(page)
        self.page = page

    # 调试用
    def __repr__(self):
        print(self.size)
        print(self.end_page)
        print(self.last_page)

        print(self.book_path)
        print(self.draft_path)
        print(self.info_path)
        return ''


class Draft(object):
    # init
    def __init__(self, size=(0, 0)):
        self.size = size
        self.buffer = numpy.zeros(self.size)

    def __repr__(self):
        print(self.buffer)
        return ''

    # empty the buffer
    def empty(self):
        self.buffer = numpy.zeros(self.size)

    def reshape(self, size):
        self.buffer = numpy.zeros(size)

    def draw(self, dot):
        self.buffer[dot] = 255


def test_book():
    b = Book()
    print(b)
    b.open_book()
    print(b)


def test_draft():
    d = Draft((8, 10))
    print(d)
    d.draw((4, 5))
    print(d)


if __name__ == '__main__':
    # dic = {
    #     'size': (800, 600),
    #     'last_page': 5,
    #     'end_page': 10,
    # }
    # with open('books/test_book/info.json', 'w') as f:
    #     s = json.dumps(dic)
    #     f.write(s)
    pass
