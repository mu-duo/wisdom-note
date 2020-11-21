import json
import numpy
from conf import *
import os
from PIL import Image


# 仅导入类 Book、Draft
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
        if 0 <= page <= self.end_page:
            self.page = page

    # 翻页，正为向后翻页， 负为向前翻页 (尽可能的翻页，直至页首或页尾）
    def turning_page(self, pages):
        pages = int(pages)
        self.page += pages
        if self.page > self.end_page:
            self.page = self.end_page
        elif self.page < 1:
            self.page = 1

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
        # 草稿尺寸
        self.size = size
        # 画笔粗细
        self.pen_size = 6
        # 缓冲区
        self.buffer = open('buffer.txt', 'w')
        # 数据文件
        self.draft = None
        # 数据转换的图片
        self.draft_image = numpy.ones((self.size[0], self.size[1], 3), numpy.uint8) * 255

    def __repr__(self):
        print(self.buffer)
        return ''

    # 将缓存区的数据写入 buffer.txt 并改名为 draft.txt
    def save_draft(self):
        self.buffer.close()
        os.remove('draft.txt')
        os.rename('buffer.txt', 'draft.txt')
        self.buffer = open('buffer.txt', 'w')

    def draw(self, data):
        # 调试用，查看输入的数据
        if DEBUG:
            print(data)

        if len(data) == 2:
            x = int(data[0][2]) // 50
            y = int(data[1][2]) // 50
            self.draft_image[x:x + self.pen_size, y: y + self.pen_size] = 0
        elif len(data) == 3:
            x = int(data[0][2]) // 50
            y = int(data[1][2]) // 50
            # 压感数值为 0 到 2047
            z = int(data[2][2]) // 8
            self.draft_image[x:x + self.pen_size, y: y + self.pen_size] = z

    # 从数据流得到图片数据
    def get_image(self):
        flag = True
        data = []
        self.draft = open('draft.txt', 'r')
        self.draft.readline().strip()
        while flag:
            s = self.draft.readline().strip()
            if s[0] == '3':
                data.append(s.split(','))
            elif s[0] == '0':
                self.draw(data)
                data.clear()
            else:
                break
        self.draft.close()

    # 保存至 draft.jpg
    def save_image(self, path=''):
        im = Image.fromarray(self.draft_image).convert('RGB')
        if path:
            im.save(path)
        else:
            im.save('draft.jpg')

    # 清空 draft_image
    def empty_image(self):
        self.draft_image = numpy.ones((self.size[0], self.size[1], 3), numpy.uint8) * 255


def test_book():
    b = Book()
    print(b)
    b.open_book()
    print(b)


def test_draft():
    d = Draft((8, 10))
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
