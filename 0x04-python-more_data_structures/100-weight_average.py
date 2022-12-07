#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for n in my_list:
            numerator += n[0] * n[1]
            denominator += n[1]
        return (numerator/denominator)
    else:
        return (0)
