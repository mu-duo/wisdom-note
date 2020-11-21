from cls import *
from evdev import InputDevice
import select
import threading
from conf import *


class WisdomNote(object):
    def __init__(self):
        self.Book = Book('test_book')
        self.Draft = Draft(self.Book.size)
        self.pen = InputDevice('/dev/input/event0')
        self.pad = InputDevice('/dev/input/event1')
        # 是否写入pen设备的数据（若不暂停会因draft.txt文件指针报错）
        self.if_write = True
        # 是否写入 draft_finish.txt，按下一次写入一次并清空buffer
        self.if_draw = False

    # 写入pen设备的数据
    def pen_run(self):
        write = False
        while self.if_write:
            select.select([self.pen], [], [])
            for event in self.pen.read():
                if event.type == 1 and event.value == 1:
                    write = True
                elif event.type == 1 and event.value == 0:
                    write = False
                if write:
                    self.Draft.buffer.write('{},{},{}\n'.format(event.type, event.code, event.value))

    # 监测pad设备是否按下
    def pad_run(self):
        while True:
            select.select([self.pad], [], [])
            for event in self.pad.read():
                # 判断是否有按键按下
                if event.type == 1 and event.value == 0:
                    if event.code == 256:
                        if DEBUG:
                            print('按键 256 被按下')
                        pass
                    if event.code == 257:
                        if DEBUG:
                            print('按键 257被按下')
                        pass
                    if event.code == 258:
                        if DEBUG:
                            print('按键 258 被按下')
                        pass
                    if event.code == 259:
                        if DEBUG:
                            print('按键 259 被按下')
                        pass
                    if event.code == 260:
                        if DEBUG:
                            print('按键 260 被按下')
                        pass
                    # 按键 261 （清空） 按下
                    if event.code == 261:
                        if DEBUG:
                            print('按键 261 被按下')
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        pass
                    # 按键 262 （上一页）按下
                    if event.code == 262:
                        if DEBUG:
                            print('按键 262 被按下')
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        self.Book.turning_page(-1)
                        pass
                    # 按键263 (下一页) 按下
                    if event.code == 263:
                        if DEBUG:
                            print('按键 263 被按下')
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        self.Book.turning_page(1)

            if self.if_draw:
                if DEBUG:
                    print('刷新缓冲区， 保存数据')
                self.Draft.save_draft()
                self.if_draw = False
                self.Draft.get_image()
                # 保存到相应的页数
                if DEBUG:
                    self.Draft.save_image()
                self.Draft.save_image('{}/draft_page_{}.jpg'.format(
                    self.Book.draft_path,
                    self.Book.page
                ))

    def run(self):
        t_pen = threading.Thread(target=self.pen_run)
        t_pad = threading.Thread(target=self.pad_run)
        t_pad.start()
        t_pen.start()


if __name__ == '__main__':
    w = WisdomNote()
    w.run()
