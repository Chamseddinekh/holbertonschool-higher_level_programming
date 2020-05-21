#!/usr/bin/python3
def safe_print_division(a, b):
    divs = None
    try:
        divs = a / b
        return divs
    except ZeroDivisionError:
        return divs
    finally:
        print("Inside result: {}".format(divs))
