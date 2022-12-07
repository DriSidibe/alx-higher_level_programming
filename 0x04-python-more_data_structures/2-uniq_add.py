#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    history = []
    for i in my_list:
        if i not in history:
            res += i
            history.append(i)
    return res
