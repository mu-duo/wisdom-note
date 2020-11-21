import threading
import time

def fun_1(a):
    while 1:
        a = '1'
        print(a)
        time.sleep(1)

def fun_2(a):
    while 1:
        a = '2'
        print(a)
        time.sleep(2)

c = ''
a = threading.Thread(target=fun_1, args=(c,))
b = threading.Thread(target=fun_2, args=(c,))
a.start()
b.start()
