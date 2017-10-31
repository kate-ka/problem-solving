
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



