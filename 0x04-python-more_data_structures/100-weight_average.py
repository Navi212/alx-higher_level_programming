#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)
    sm = 0
    av = 0
    for i in my_list:
        sm += i[0] * i[1]
        av += i[1]
    return (sm / av)
