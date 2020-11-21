def main():
    f = open('/dev/input/event0', 'r+')
    a =  f.read()
    for i in a:
        print(a)


main()
