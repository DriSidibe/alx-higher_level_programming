#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    l = []
    for i in my_list:
        if i not in l:
            res += i
            l.append(i)
    return res
