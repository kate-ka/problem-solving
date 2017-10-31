"""
Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by
 different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 238.
---Part 2 ---
Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx,
 abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats
with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between,
 even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

Your puzzle answer was 69.

"""

import re


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

