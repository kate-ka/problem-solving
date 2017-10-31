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






