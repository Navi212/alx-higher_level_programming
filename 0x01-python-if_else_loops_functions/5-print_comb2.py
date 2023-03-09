#!/usr/bin/python3
zero = 0
for i in range(0, 99 + 1):
    if i < 10:
        print("{:02d}".format(i), end=", ")
    if i > 9 and i < 99:
        print("{}".format(i), end=", ")
    if i == 99:
        print("{}".format(i))
