import re
import numpy as np

regex = re.compile('([a-z\s]+)\s([0-9]+),([0-9]+)\sthrough\s([0-9]+),([0-9]+)')
grid = np.zeros((1000, 1000))
with open('day6.txt', 'r') as f:
    for line in f.readlines():
        command, x1, y1, x2, y2 = re.search(regex, line).groups()
        for y in range(int(y1), int(y2)+1):
            for x in range(int(x1), int(x2)+1):
                if command == 'turn on':
                    grid[y][x] += 1

                elif command == 'toggle':
                    grid[y][x] += 2

                elif command == 'turn off':
                    if grid[y][x] > 1:
                        grid[y][x] -= 1
                    else:
                        grid[y][x] = 0

print(np.sum(grid))
# z = []
# for item in grid:
#     z.append(sum(item))
# print(sum(z))#17836115


