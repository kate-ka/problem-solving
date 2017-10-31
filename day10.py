"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading
aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as
"one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step.
 For each step, take the previous value, and replace each run of digits (like 111) with the number of
 digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle answer was 329356.

--- Part Two ---

Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of
Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the
length of the new result?

Your puzzle answer was 4666278.

"""


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
    nums = list(chain.from_iterable((len(list(g)),int(k)) for k, g in groupby(inp)))
    return nums


def look_and_say4(inp='3113322113', count=40):
    for i in range(count):
        inp = look_and_say3(inp)

    return inp
print(len(look_and_say4())) #329356




