"""Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him
via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
Your puzzle answer was 2592."""


with open('day3.txt', 'r') as f:
    x, y = 0, 0
    present = 1
    coords = []
    for item in f.read():
        if item == '^':
            y += 1
        if item == 'v':
            y -= 1
        if item == '>':
            x += 1
        if item == '<':
            x -= 1
        if (x, y) not in coords:
            coords.append((x,y))
    # to append the last coords
    coords.append((x,y))
    print (len(coords)) # 2592

""" Part 2"""
# If Santa had an assistant who could go parallel
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


chars = open('day3.txt', 'r').read()
import re
directions = re.findall('.{2}', chars)
x1, y1 = 0, 0
x2, y2 = 0, 0
coords1= []
coords2 = []

for coord in directions:

    if coord[0] == '^':
        y1 += 1
    if coord[0] == 'v':
        y1 -= 1
    if coord[0] == '>':
        x1 += 1
    if coord[0] == '<':
        x1 -= 1
    if coord[1] == '^':
        y2 += 1
    if coord[1] == 'v':
        y2 -= 1
    if coord[1] == '>':
        x2 += 1
    if coord[1] == '<':
        x2 -= 1
    if (x1, y1) not in coords1:
            coords1.append((x1,y1))
    if (x2, y2) not in coords2:
            coords2.append((x2,y2))
print(len(set(coords1 + coords2))) # 2360






