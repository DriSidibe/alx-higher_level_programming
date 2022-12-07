#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for name in sorted(a_dictionary):
        print("{}: {}".format(name, a_dictionary[name]))
