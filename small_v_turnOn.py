a = [[0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)],
     [0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)]]
print(a[0][10])

for item_list in a:
    for i in range(len(item_list)):
        item_list[i] = 1
print(a)

for item_list in a:
    item_list[0] = 0
print(a)

for i in range(len(a)):

    for i in range(len(a[0])):
        a[4][3] = 0
        a[4][4] = 0
        a[5][3] = 0
        a[5][4] = 0
print(a)

z= []
for item in a:
    z.append(sum(item))
print(sum(z))

