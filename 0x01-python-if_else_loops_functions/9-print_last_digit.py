def print_last_digit(number):
    if number < 0:
        res = abs(number) % 10
    else:
        res = number % 10
    print("{:d}".format(res), end='')
    return res
