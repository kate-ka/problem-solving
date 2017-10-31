import numpy as np

def rectangle_parity(size):
    lights = np.zeros((size,size),dtype=np.int)
    midpoint = size/2
    x = 0
    for y in range(size):
        if y <= midpoint:
            lights[y][midpoint - x] = 1

            lights[y][midpoint + x] = 1
            if y != midpoint:
                x += 1
        if y > midpoint:
            if y == size - 1:
                lights[y][midpoint] = 1
            else:
                x = x - 1
                lights[y][midpoint + x] = 1
                lights[y][midpoint - x] = 1


    for r in lights:
        np.set_printoptions(threshold=np.nan)
        print r

rectangle_parity(9)