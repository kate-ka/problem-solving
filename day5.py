import re

# regexp = re.compile(r"(.)\1")
# data = ["parrot","follia","carrot","mattia","rettoo","melone"]
#
# for str in data:
#     match = re.search(regexp, str)
#     if match:
#         print (str, "<- match for double", match.group(1))
#     else:
#         print (str, "<- doesn't match")
#
# s = 'ugknbfddgicrmopn'
# r = re.compile(r"(.)\1")
# match = re.search(r, s)
# print(match.group())
#
# print (re.search('(ab)|(cd)|(pg)|(xy)','ffgab').group())



def check_str():
    nice_strings = []
    regex1 = re.compile(r'(ab)|(cd)|(pq)|(xy)')
    regex2 = re.compile(r"(.)\1")
    regex3 = re.compile(r'[aeiou]')
    with open('day5.txt', 'r') as f:

        for item in f.readlines():
            # nice string does not contain ab, cd, pq, xy
            if re.search(regex1, item):
                 continue
            else:
                if re.search(regex2, item):
                    # nice string has at least 3 vowels
                    if len(re.findall(regex3, item)) >= 3:
                        nice_strings.append(item)

    print(len(nice_strings))

check_str() # 238

def check_str2():
    nice_strings = []
    regex1= re.compile(r'([\w][\w])(.)*\1') # two different doubling characters eg xygxy
    regex2 = re.compile(r'(\w).\1') # eg xyx, ztz, vtv
    with open('day5.txt', 'r') as f:
        for item in f.readlines():
            if re.search(regex1, item) and re.search(regex2, item):
                nice_strings.append(item)
    print(len(nice_strings))

check_str2()

