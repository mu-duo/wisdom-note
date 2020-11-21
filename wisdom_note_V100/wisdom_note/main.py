from evdev import InputDevice
import select
from threading import Thread, Lock
import time

pen = InputDevice('/dev/input/event0')
pad = InputDevice('/dev/input/event8')
f = open('info.txt', 'w')


def check(dev, type_list=None, code_list=None):
    if type_list:
        while True:
            select.select([dev], [], [])
            for event in dev.read():
                if event.type in type_list: # and event.code in code_list:
                    print(f'type:{event.type} code:{event.code} value:{event.value}')
                    f.write('type:{} code:{} value:{}\n'.format(event.type, event.code, event.value))
            time.sleep(0.0000000000000001)
    else:
        while True:
            select.select([dev], [], [])
            for event in dev.read():
                print(f'type:{event.type} code:{event.code} value:{event.value}')
                f.write('type:{} code:{} value:{}\n'.format(event.type, event.code, event.value))
            time.sleep(0.0000000000000001)


if __name__ == '__main__':
    # t1 = Thread(target=check, args=(pad, (), ()))
    t2 = Thread(target=check, args=(pen, (1,), (0,1,3)))
    # t1.start()
    t2.start()

