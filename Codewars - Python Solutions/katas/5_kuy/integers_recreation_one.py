# def list_squared(m, n):
#     Examples:
    #
    # list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
    # list_squared(42, 250) --> [[42, 2500], [246, 84100]]
import math

n = 250
m = 1

res = []
counter = 0
for item in [i**2 for i in range(m, n+1) if n%i==0]:
    counter+= item
    if not math.sqrt(counter)-int(math.sqrt(counter)):
        res.append(counter)

print(res)
