#!/usr/bin/python3
import sys


def cmd_line():
    sum_args = len(sys.argv) - 1

    if (sum_args == 0):
        print("{} arguments.".format(sum_args))
    elif (sum_args == 1):
        print("{} argument:".format(sum_args))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(sum_args))
        for i in range(1, sum_args+1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    cmd_line()
