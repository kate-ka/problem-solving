from collections import OrderedDict


def ordered_count(input):
    """Count the number of occurencences of each character
    and return it as a list of tuples in order of appearance.
    Example:
        ordered_count("abracadabra") ==
        [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]"""
    occurences = OrderedDict()
    for item in input:
        occurences.setdefault(item, 0)
        occurences[item] += 1
    return [(key, occurences[key]) for key in occurences]