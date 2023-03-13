#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first char"""

    i = 0
    str_len = len(sentence)
    if str_len < 1:
        return str_len, None
    else:
        return str_len, sentence[i]
