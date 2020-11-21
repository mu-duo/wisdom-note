from cls import *
from evdev import InputDevice
import select
import threading


class WisdomNote(object):
    def __init__(self):
        self.Book = Book('test_book')
        self.Draft = Draft(self.Book.size)
        self.pen = InputDevice('/dev/input/event0')
        self.pad = InputDevice('/dev/input/event1')
        self.if_write = True
        self.if_draw = False

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

    def pad_run(self):
        while True:
            select.select([self.pad], [], [])
            for event in self.pad.read():
                if event.type == 1 and event.value == 0:
                    if event.code == 256:
                        pass
                    if event.code == 257:
                        pass
                    if event.code == 258:
                        pass
                    if event.code == 259:
                        pass
                    if event.code == 260:
                        pass
                    if event.code == 261:
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        pass
                    if event.code == 262:
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        self.Book.turning_page(-1)
                        pass
                    if event.code == 263:
                        self.if_write = bool(1 - self.if_write)
                        self.if_draw = True
                        self.Book.turning_page(1)

            if self.if_draw:
                self.Draft.save_draft()
                self.if_draw = False
                self.Draft.get_image()
                self.Draft.save_image()

    def run(self):
        t_pen = threading.Thread(target=self.pen_run)
        t_pad = threading.Thread(target=self.pad_run)
        t_pad.start()
        t_pen.start()


if __name__ == '__main__':
    w = WisdomNote()
    w.run()
