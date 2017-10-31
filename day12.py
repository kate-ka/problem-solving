
import json
x = json.loads(open('day12.txt', 'r').read())


 #111754 without 'red' - 65402

#print(parse(x))

def parse(item):
    if isinstance(item, int):
        return item

    elif isinstance(item, dict):
        item = item.values()
        if 'red' in item:
            return 0

    return sum(parse(i) for i in item if type(i) != str)

#print(parse(x))


def parse_stack(items):
    stack = [items]
    count = 0

    while stack:
        item = stack.pop()

        if isinstance(item, dict):
            stack += item.values()
        elif isinstance(item, list):
            stack += item
        elif isinstance(item, int):
            count += item

    return count

print(parse_stack(x))
# print(parse_stack({'a': [2,3, [1,2]], 'b': [1,2,3]}))
#print(parse_stack(x))