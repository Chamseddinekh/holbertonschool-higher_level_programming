#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            elem += 1
    except IndexError:
        print('')
        return elem
    else:
        print('')
        return elem
