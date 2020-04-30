#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    sum_argv = 0
    length = len(sys.argv)
    for i in range(i, length):
        sum_argv += int(sys.argv[i])
        i += 1
    print("{}".format(sum_argv))
