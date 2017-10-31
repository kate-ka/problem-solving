"""Implement a document scanning engine that receives a text document "doc" and returns a list
of all unique words in it and their number of occurrences, sorted by the number of occurrences
in descending order.

Example:
for doc: "practice makes perfect. get perfect by practice. just practice!"
the engine returns the list: { practice: 3, perfect: 2, makes: 1, get: 1, by: 1, just: 1 }.

The engine should ignore punctuation and white-spaces.
Find the minimal runtime complexity and analyze it."""
import collections

import re

def scanning_doc(doc):

    depanctuted_doc= re.sub(r'[!:;?\.,\'\"]', '', doc)
    return collections.Counter(depanctuted_doc.split())



def count_word_occurencies(doc):

    words_occurrences = {}
    depanctuted_doc = re.sub(r'[!:;?\.,\'\"]', '', doc)

    for word in depanctuted_doc.split():
        if word in words_occurrences:
            words_occurrences[word] += 1
        words_occurrences.setdefault(word, 1)


    or_d = collections.OrderedDict((sorted(words_occurrences.items(), key=lambda x: x[1], reverse=True)))
    return or_d

# print(count_word_occurencies("practice makes perfect. get get get get get perfect by practice. just practice!"))
# print(scanning_doc("practice makes perfect. get get get get get perfect by practice. just practice!"))


def my_split(doc):
    start = 0
    end = 0
    delimeters = ('.', ' ', '?')
    result = []
    for i in range(len(doc)):
        if doc[i] in delimeters:
            if end - start > 0:
                result.append(doc[start:end+1])
            start = end + 2
        end = i
    else:
        if end - start > 0:
            result.append(doc[start: end+1])

    return result


# print(my_split('deа ollolo..'))