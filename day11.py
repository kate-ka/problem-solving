"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a
method of coming up with a password based on the previous one. Corporate policy dictates
that passwords must be exactly eight lowercase letters (for security reasons), so he finds
 his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase
 the rightmost letter one step; if it was z, it wraps around to a, and repeat with the
 next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some
additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc,
bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken
for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij)
but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the
 passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle answer was vzbxxyzz.
"""
letters = 'abcdefghijklmnopqrstuvwxyz'
doubles = [c+c for c in letters]
straights = [''.join(t) for t in zip(letters[:-2], letters[1:-1], letters[2:])]
next_letter = {c1: c2 for c1, c2 in zip(letters, letters[1:]+'a')}


def is_valid(s):
    # cannot contain i, o, or l
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    # must include two different pairs of letters
    if sum([d in s for d in doubles]) < 2:
        return False
    # must include a straight of length 3 or greater
    if not any([d in s for d in straights]):
        return False
    return True


def next_password(s):
    s = s[:-1] + next_letter[s[-1]]  # increment the last letter
    for i in range(-1, -8, -1):
        if s[i] == 'a':  # increment n-1 letter if n letter changed to 'a'
            s = s[:i-1] + next_letter[s[i-1]] + s[i:]
        else:
            break
    return s


password = "vzbxkghb"
while is_valid(password) == False:
    password = next_password(password)
print(password) #vzbxxyzz

print(next_password('vzbxxyzz'))