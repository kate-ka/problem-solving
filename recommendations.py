import operator

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# Returns a distanse-based similarity score for person1 and person2
from math import sqrt


def sim_distance(prefs, person1, person2):
    # Get the list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares =sqrt(sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]]))
    return 1/(1+sum_of_squares)

print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    # Find the number of elements
    n = len(si)

    # if they are no ratings in common, return 0
    if n == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # print(sum1, sum2)  18.0 19.5

    # Sum up all the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum up the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate the Pearson score
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r

print (sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    # Sort the list so the highest scores appear at the top

    return sorted(scores, reverse=True)[0:n]

print(topMatches(critics, 'Toby', n=3))

# X = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "a"]
# Y = [ 0,   11,   1,    0,   1,   2,   2,   0,   1, 1]
# print([x for (y,x) in sorted(zip(Y,X))])
# print(sorted(zip(Y,X)))
# print([x for (y, x) in sorted(zip(Y, X), key=lambda i: i[0])])
# print(sorted(zip(Y, X), key=lambda i: i[0]))
# print(list(zip(*sorted(list((zip(X,Y))), key=operator.itemgetter(1))))[0])

# Gets recommendations for a person by using a weighted average
# of every other user's rankings


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person]or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
        # Create the normalized list
        rankings = [(total/simSums[item], item) for item, total in totals.items()]
        # return the sorted list
        return sorted(rankings, reverse=True)
print(getRecommendations(critics, 'Toby', similarity=sim_distance))

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

print(transformPrefs(critics))
# let's find movies similar to 'Superman Returns'
movies = transformPrefs(critics)
print(topMatches(movies, 'Superman Returns'))

# Let's find recommended critics for the movie to invite them to the premier
print(getRecommendations(movies, 'Just My Luck'))

# (-0.07636310947619934, 'metallist-ka', u'Marissa_Jones')
# 0
# 0
# (-0.0470868803758812, 'metallist-ka', u'theholte')
# (-0.11779310585103435, 'metallist-ka', u'Jajczu')
# (0.0333316676838547, 'metallist-ka', u'MetalPumpkin')
# (-0.1678135601747674, 'metallist-ka', u'plantmywife')


# [(0.0333316676838547, u'MetalPumpkin'), (0, u'ohsoococo'), (0, u'Amaretati'),
#  (-0.0470868803758812, u'theholte'), (-0.07636310947619934, u'Marissa_Jones'),
#  (-0.11779310585103435, u'Jajczu'), (-0.1678135601747674, u'plantmywife')] pearson
#
#
# [(0.5, u'Amaretati'), (0.0192271445518752, u'Jajczu'), (0.008435865511351495, u'plantmywife'),
#  (0.005621904569202427, u'theholte'), (0.005230272223712981, u'Marissa_Jones'), (0.0043665195299183055, u'MetalPumpkin'),
#  (0, u'ohsoococo')] sim distance
