import numpy as np


lights = np.zeros((10,10),dtype=np.int)

# lights[0][0] = 1
# lights[1][0] = 1
# lights[1][1] = 1
# lights[2][0] = 1
# lights[2][1] = 1
# lights[2][2] = 1
# lights[3][0] = 1
# lights[3][1] = 1
# lights[3][2] = 1
# lights[3][3] = 1



# def rectangle(size):
#     lights = np.zeros((size,size),dtype=np.int)
#     for y in range(0, size):
#         for x in range(y+1):
#              lights[y][x] = 1
#     for r in lights:
#         np.set_printoptions(threshold=np.nan)
#         print r


# rectangle(10)

# def rectangle_triangle(size):
#     lights = np.zeros((size,size),dtype=np.int)
#     for y in range(0, size):
#         for x in range(y+1, size):
#              lights[y][x] = 1
#
#     for r in lights:
#         np.set_printoptions(threshold=np.nan)
#         print r

# rectangle_triangle(100)

# def rectangle_cross(size):
#     lights = np.zeros((size,size),dtype=np.int)
#     y= 0
#     for x in range(size):
#         lights[(size/2)-1][x] = 1
#         lights[size/2][x] = 1
#         lights[y][(size/2)-1] = 1
#         lights[y][(size/2)] = 1
#         y+=1
#
#
#     for r in lights:
#         np.set_printoptions(threshold=np.nan)
#         print r
#
# rectangle_cross(10)

# def rectangle_cross(size):
#     lights = np.zeros((size,size),dtype=np.int)
#     y = 0
#     for x in range(size):
#         lights[size/2][x] = 1
#         lights[y][size/2] = 1
#
#         if y in range(1, size-1):
#             for x in range(1, size-1):
#                 lights[y][x] = 1
#
#         y += 1
#     for r in lights:
#         np.set_printoptions(threshold=np.nan)
#         print r
#
# rectangle_cross(7)

def rectangle_parity(size):
    lights = np.zeros((size,size),dtype=np.int)
    midpoint = size/2
    for y in range(size/2+1):
        if y <= midpoint:
            lights[y][midpoint - y] = 1
            lights[y][midpoint + y] = 1
    print range(size-1, midpoint, -1)

    x = 1
    for y in range(size-1, midpoint, -1):
        if y == size - 1:
            lights[y][midpoint] = 1
        else:
            lights[y][midpoint - x] = 1
            lights[y][midpoint + x] = 1
            x += 1








    for r in lights:
        np.set_printoptions(threshold=np.nan)
        print r

rectangle_parity(9)


