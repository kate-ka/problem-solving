# 1. Write a Python script to sort (ascending and descending) a dictionary by value. -
#  See more at: http://www.w3resource.com/python-exercises/dictionary/#EDITOR
import operator


def sort_dict(d):
    import operator
    from collections import OrderedDict
    sorted_dict = OrderedDict(sorted(d.items(), key=operator.itemgetter(0), reverse=True))

    return sorted_dict

# print(sort_dict({'cat': 4, 'dog':3, 'marsik': 5}))


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g


# print(itemgetter(1)('ABCDEFG'))
# itemgetter(1,3,5)('ABCDEFG')
# ('B', 'D', 'F')
# >>> itemgetter(slice(2,None))('ABCDEFG')
# 'CDEFG'

# Write a Python script to add key to a dictionary. Go to the editor
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
#


student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}
results = {} # removing duplicates
for key,value in student_data.items():
    if value not in results.values():
        results[key] = value

# print(results)

def sum_recur(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_recur(l[1:])

# print(sum_recur([1, 2, 3, 4, 5]))


def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]


# print(to_string(2835,16))


x = [1, 2, [3,4], [5,6]] #21, list sum
def sum_r(x):
    count = 0
    for i in x:
        if isinstance(i, int):
            count += i
        elif isinstance(i, list):
            count += sum_recur(i)
    return count
print(sum_r(x))


def factorial(n):
    if n <= 1:

        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        return (fib(n - 1) + (fib(n - 2)))

# print(fib(7))


def sumDigits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sumDigits(number/10)

print(sumDigits(345))


#  n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
# Test Data :
# sum_series(6) -> 12


def summarize(n):
    if n < 1:
        return 0
    else:
        return n + summarize(n-2)


def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))

# print(harmonic_sum(7))
# print(harmonic_sum(4))