import re

grid = []

for i in range(0, 1000):
    unit = [0 for x in range(0, 1000)]
    grid.append(unit)
# print(grid[489][959])




def read_commands():
    with open('commands.txt', 'r') as f:
        for item in f.readlines():

            if (re.search('[A-Za-z]+(\s[A-Za-z]+)?', item).group()) == 'turn on':
                turn_on_the_lights((re.findall('[0-9]+,[0-9]+', item))[0], (re.findall('[0-9]+,[0-9]+', item))[1])
            elif (re.search('[A-Za-z]+(\s[A-Za-z]+)?', item).group()) == 'turn off':
                turn_off_the_lights((re.findall('[0-9]+,[0-9]+', item))[0], (re.findall('[0-9]+,[0-9]+', item))[1])
            else:
                toggle((re.findall('[0-9]+,[0-9]+', item))[0], (re.findall('[0-9]+,[0-9]+', item))[1])
    return


def turn_on_the_lights(start, stop):
    x1, y1 = start.split(',')
    print(x1,y1)
    x2, y2 = stop.split(',')

    for i in range(int(y1), int(y2) + 1):
        for k in range(int(x1), int(x2) + 1):
            grid[i][k] = 1



def turn_off_the_lights(start, stop):
    x1, y1 = start.split(',')
    x2, y2 = stop.split(',')

    for i in range(int(y1), int(y2) + 1):
        for k in range(int(x1), int(x2) + 1):
            grid[i][k] = 0


    return


def toggle(start, stop):
    x1, y1 = start.split(',')
    x2, y2 = stop.split(',')

    for i in range(int(y1), int(y2) + 1):
        for k in range(int(x1), int(x2) + 1):
            if grid[i][k] == 1:
                grid[i][k] = 0
            else:
                grid[i][k] = 1

    return
read_commands()





count = len([item for row in grid for item in row if item==1])

print(count)
