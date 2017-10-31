"""
Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every
 pair of locations. He can start and end at any two (different) locations he wants, but he must visit each
 location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 141.

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Your puzzle answer was 736.
"""
from itertools import permutations
import re


def parse_data(file):
    with open(file, 'rt') as f:
        cities = set()
        distances = {}

        for line in f.readlines():
            city1, city2, distance = re.search('^([a-zA-z]+)\sto\s([a-zA-Z]+)\s=\s([0-9]+)$', line).groups()
            distances[city1, city2] = distance
            distances[city2, city1] = distance
            cities.add(city1)
            cities.add(city2)

    return cities, distances


def find_min_route(cities, distances):
    possible_routes = permutations(cities)
    routes = []

    for item in possible_routes:
        route = sum(
            int(distances[item[i], item[i+1]])
            for i in range(len(item)-1)
        )

        routes.append((route, item))

    return min(routes)

data = parse_data('day9.txt')
cities = data[0]
distances = data[1]

print(find_min_route(cities, distances)) # 141



