def look_and_say(inp='3113322113'):
    start = inp[0]
    repeated_nums = []
    result = ''
    for i in inp:
        if i == start:
            repeated_nums.append(i)

        else:
            result = result + str(len(repeated_nums))+ repeated_nums[0]
            repeated_nums = []
            repeated_nums.append(i)
            start = i
    result = result + str(len(repeated_nums)) + repeated_nums[0]
    return result


def look_and_say2(inp='3113322113', count=40):
    for i in range(count):
        inp = look_and_say(inp)

    return inp

# print(len(look_and_say2()))#329356


def look_and_say3(inp='3113322113'):
    from itertools import groupby, chain
#     * is the "splat" operator: It takes a list as input, and expands it into actual positional arguments in the function call.
#
# So if uniqueCrossTabs was [ [ 1, 2 ], [ 3, 4 ] ], then itertools.chain(*uniqueCrossTabs) is the same as
# saying itertools.chain([ 1, 2 ], [ 3, 4 ])


    # nums = list(chain(*[(len(list(g)),int(k)) for k, g in groupby(inp)]))
    # or
    nums = list(chain.from_iterable((len(list(g)),int(k)) for k, g in groupby(inp)))
    return nums

def look_and_say4(inp='3113322113', count=40):
    for i in range(count):
        inp = look_and_say3(inp)

    return inp
print(len(look_and_say4())) #329356




