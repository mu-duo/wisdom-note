from evdev import InputDevice
from select import select
import time


pen = InputDevice('/dev/input/event0')
pad = InputDevice('/dev/input/event1')

def check(dev):
    while True:
        select([dev], [], [])
        for event in dev.read():
        #if event.type == 3 and event.code in [0,1]: 
            print(event.code, '---', event.type, '---', event.value)

check(pen)
