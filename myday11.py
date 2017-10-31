letters = 'abcdefghijklmnopqrstuvwxyz'
doubles = [letter + letter for letter in letters]
straights =[''.join(item) for item in zip(letters[:-2], letters[1:], letters[2:])]


def is_valid(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    if sum([double in s for double in doubles]) < 2:
        return False
    if not any([straight in s for straight in straights]):
        return False


def inc_letter(l):
    if l == 'z':
        return 'a'

    return letters[letters.find(l) + 1]

def incr(s): #hijklmmn
    if s[-1] == 'z':
        d = incr(s[:-1]) + inc_letter('z')
    else:
        d = s[:-1] + inc_letter(s[-1])

    return d



password = 'vzbxkghb'

# print(incr('aaa'))
# print(incr('aab'))
# print(incr('aac'))
# print(incr('aaz'))
while is_valid(password) == False:
    password = incr(password)
print(password)



def merge_sort(l):

    if len(l) == 1:
        return l

    middle = int(len(l) / 2)

    sorted_left = merge_sort(l[0:middle])
    sorted_right = merge_sort(l[middle:len(l)])

    merged = []

    while sorted_left and sorted_right:
        if sorted_left[0] > sorted_right[0]:
            merged.append(sorted_right.pop(0))
        else:
            merged.append(sorted_left.pop(0))

    if sorted_right:
        merged += sorted_right
    elif sorted_left:
        merged += sorted_left

    return merged




print(merge_sort([81,66, 3, 334,2,3,6,7,4,5,1]))

