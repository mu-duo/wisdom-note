from cls import *
from evdev import InputDevice
import select


class WisdomNote(object):
    def __init__(self):
        self.Book = Book('test_book')
        self.Draft = Draft()
        self.pen = InputDevice('/dev/input/event0')
        self.pad = InputDevice('/dev/input/event0')

    def run(self):
        flag = False
        data = []
        while True:
            select.select([self.pen], [], [])
            for event in self.pen.read():
                if event.type == 1 and event.value == 1:
                    flag = True
                elif event.type == 1 and event.value == 0:
                    flag = False
                if flag and event.type == 3:
                    if event.code in [1,0]:
                        data.append(event.value)
                elif flag and event.type == 0:
                    print(data)
                    data.clear()


if __name__ == '__main__':
    w = WisdomNote()
    w.run()