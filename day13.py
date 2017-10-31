from itertools import permutations
from collections import defaultdict


# def parse1(filename):
#     combinations = {}
#     with open(filename, 'r') as f:
#         for line in f.readlines():
#             line = line.split()
#             guest1 = line[0]
#             guest2 = line[10][:-1]
#             op = line[2]
#             hap = line[3]
#             combinations.setdefault(guest1, {})
#             if op == 'gain':
#
#                 combinations[guest1][guest2] = hap
#             else:
#                 combinations[guest1][guest2] = int(hap) * -1
#     return combinations

# def parse2(filename):
#     combinations = {}
#     with open(filename, 'r') as f:
#         for line in f.readlines():
#             line = line.split()
#             guest1 = line[0]
#             guest2 = line[10][:-1]
#             op = line[2]
#             hap = line[3]
#             if guest1 not in combinations:
#                 combinations[guest1] = {}
#
#             if op =='gain':
#                 combinations[guest1][guest2] = int(hap)
#             if op == 'lose':
#                 combinations[guest1][guest2] = int(hap) * -1
#
#     return combinations

def parse(filename):
    combinations = defaultdict(dict)

    with open(filename, 'r') as f:
        for line in f.readlines():
            guest1, __, operation, hap, *__, guest2 = line.split()
            combinations[guest1][guest2] = int(hap) if operation == 'gain' else -int(hap)

    guests = tuple(combinations.keys())
    for guest in guests:
        combinations['me'][guest] = 0

    return combinations


def prepare_couples():
    s = []
    people = parse('day13.txt')
    guests = people.keys()

    possible_seats = permutations(guests)

    for perm in possible_seats:
        count = 0

        for i in range(len(perm)):
            count += people[perm[i]].get(perm[i-1], 0)
            count += people[perm[i-1]].get(perm[i], 0)

        s.append(count)

    return max(s)

print(prepare_couples())







