#-*- coding: utf-8
from operator import itemgetter
from collections import OrderedDict
from itertools import filterfalse, groupby
import pprint


def my_groupby(iterable, key):
    results = OrderedDict()

    for item in iterable:
        if key(item) not in results:
            results[key(item)] = []
            results[key(item)].append(item)
        else:
            results[key(item)].append(item)
    return results.items()


def my_groupby_2(iterable, key):
    results = []
    prev_key = key(iterable[0])

    grouped = []
    for item in iterable:
        if key(item) != prev_key:
            results.append((prev_key, grouped))
            prev_key = key(item)

            grouped = []

        grouped.append(item)

    results.append((prev_key, grouped))
    return results


# results.append((k, value))
# results.append((prev_key, []))
# results[key(prev_key)].append(item)

countries = [
    ['USA', 'New York', 4534, 2016],
    ['USA', 'Dallas', 444, 2016],
    ['USA', 'Dallas', 345, 2015],
    ['USA', 'Denver', 533, 2015],
    ['USA', 'Kansas', 555, 2015],
    ['USA', 'New York', 4454, 2015],
    ['Ukraine', 'Kyiv', 55, 2016],
    ['Ukraine', 'Kyiv', 44,  2015],
    ['Ukraine', 'Lviv', 34, 2016],
    ['Ukraine', 'Lviv', 22,  2015],
    ['Slovakia', 'Misto1', 34, 2014],
    ['Slovakia', 'Misto2', 45, 2013]
]

sorted_countries = sorted(countries, key=lambda x: x[3])
# pprint.pprint (sorted_countries)
pprint.pprint( my_groupby_2(sorted_countries, lambda item: '{}_{}'.format(item[0], item[3])))


data = [
    {'key': 'one', 'value': 1},
    {'key': 'one', 'value': 1},
    {'key': 'two', 'value': 2},
    {'key': 'two', 'value': 2},
    {'key': 'three', 'value': 3}
]

# print my_groupby(data, lambda item: (item['key'], item['value']))


# [
#     ('one', [{'key': 'one', 'value': 1}, {'key': 'one', 'value': 1}]),
#     ('two', [{'key': 'two', 'value': 2}, {'key': 'two', 'value': 2}]),
#     ('three', [{'key': 'one', 'value': 3}]),
# ]


# 1 group by country
# 2. group by country and year
# 3. group by city
# 4 group by country and city

# print my_groupby(countries, lambda item: (item[0], item[3]))

# [( ('USA', 2016),
#   [ ['USA', 'New York', 4534, 2016], ['USA', 'Dallas', 444, 2016] ]),
#  (('USA', 2015),
#   [['USA', 'Dallas', 345, 2015],
#    ['USA', 'Denver', 533, 2015],
#    ['USA', 'Kansas', 555, 2015],
#    ['USA', 'New York', 4454, 2015]]),
#  (('Ukraine', 2016), [['Ukraine', 'Kyiv', 55, 2016]]),
#  (('Ukraine', 2015), [['Ukraine', 'Kyiv', 44, 2015]]),
#  (('Ukraine', 2016), [['Ukraine', 'Lviv', 34, 2016]]),
#  (('Ukraine', 2015), [['Ukraine', 'Lviv', 22, 2015]])]
#
#
# list((k, list(g)) for k, g in groupby(countries, lambda x: (x[0], x[3])) )
# [(('USA', 2016), [['USA', 'New York', 4534, 2016], ['USA', 'Dallas', 444, 2016]]), (('USA', 2015), [['USA', 'Dallas', 345, 2015], ['USA', 'Denver', 533, 2015], ['USA', 'Kansas', 555, 2015], ['USA', 'New York', 4454, 2015]]), (('Ukraine', 2016), [['Ukraine', 'Kyiv', 55, 2016]]), (('Ukraine', 2015), [['Ukraine', 'Kyiv', 44, 2015]]), (('Ukraine', 2016), [['Ukraine', 'Lviv', 34, 2016]]), (('Ukraine', 2015), [['Ukraine', 'Lviv', 22, 2015]])]


def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

# print(list(unique_everseen('ABBCcAD', str.lower)))

def my_unique(iterable, key=None):
    unque_values = []

    if key is None:
        for item in iterable:
            if item not in unque_values:
                unque_values.append(item)
    else:
        keys = []
        for item in iterable:
            k = key(item)
            if k not in keys:
                keys.append(k)
                unque_values.append(item)
    return unque_values


# print(my_unique('ABBCcAD', str.lower))


def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return map(next, map(itemgetter(1), groupby(iterable, key)))

# print (list((unique_justseen('ABBCcAD', str.lower))))


def my_unique_justseen(iterable, key=None):
    prev_item = iterable[0]
    results = []

    if not key:
        key = lambda item: item

    prev_key = key(prev_item)

    for item in iterable:
        if key(item) != prev_key:
            results.append(prev_item)
            prev_item = item
            prev_key = key(item)


    results.append(prev_item)

    return results

print(my_unique_justseen('ABBCcAD', str.lower))