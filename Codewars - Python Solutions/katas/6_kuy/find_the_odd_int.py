"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
from itertools import groupby


def find_it(seq):

    for number, group in groupby(sorted(seq)):
        if len(list(group)) % 2 != 0:
            return number
    return None