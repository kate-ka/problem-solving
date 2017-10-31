import re

grid = []

for i in range(0, 1000):
    unit = [0 for x in range(0, 1000)]
    grid.append(unit)

def read_commands():
    reg = r'([A-Za-z\s]+)\s([0-9]+),([0-9]+)\sthrough\s([0-9]+),([0-9]+)'

    with open('commands.txt', 'r') as f:
        for item in f.readlines():
            command, x1, y1, x2, y2 = re.search(reg, item).groups()
            # print(x1, y1)

            for i in range(int(y1), int(y2) + 1):
                for k in range(int(x1), int(x2) + 1):
                    if command == 'turn on':
                        grid[i][k] = 1
                    elif command == 'turn off':
                        grid[i][k] = 0
                    else:
                        # toggle
                        grid[i][k] = int(not grid[i][k])


read_commands()
count = len([item for row in grid for item in row if item == 1])

print(count)

