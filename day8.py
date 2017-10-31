STRING = open('day8.txt', 'rb')

count = 0
new_lines  = 0

for item in STRING.readlines():

    # string-escape removes extra slashes that python adds to prevent string break (for python 2.7)
    #x = item.decode('string-escape')[1:-2]
    print(item)

    x = item.decode('unicode_escape').replace('\n', '')[1:-1]
    # n = str(item).replace('\n', '').replace("\\", '\\\\').replace('"', '\\"')
    # n = '"{}"'.format(n)
    # new_lines += len(n)


    count += len(x)
print(count, end= ' Count\n')
print(new_lines)

# print(count)
STRING = open('day8.txt', 'r').readlines()

count_2 = 0
for item in STRING:
    item = item.replace('\n', '')
    count_2 += len(item)
    # item = item.replace('\\', '\\\\').replace('"', '\\"')
    # print(item)


print (count_2 - count) # 1342
part2 = open('day8.txt', 'r')
count = 0
count2 = 0
for item in part2.readlines():
    count2 += len(item.replace('\n', ''))
    n = item.replace('\n', '').replace("\\", '\\\\').replace('"', '\\"')
    n = '"{}"'.format(n)
    count += len(n)
print(count - count2)#2074