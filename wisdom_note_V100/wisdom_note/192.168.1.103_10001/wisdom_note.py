from cls import *
from evdev import InputDevice
import select
import time


class WisdomNote(object):
    def __init__(self):
        self.Book = Book('test_book')
        self.Draft = Draft()
        self.dev = InputDevice('/dev/input/event0')

    def run(self):
        flag = False
        data = []
        while True:
            select.select([self.dev], [], [])
            for event in self.dev.read():
#                if event.type == 1 and event.value == 1:
#                    flag = True
#                elif event.type == 1 and event.value == 0:
#                    flag = False
#                if flag and event.type == 3:
                print(event.type, event.code, event.value)


if __name__ == '__main__':
    w = WisdomNote()
    w.run()
