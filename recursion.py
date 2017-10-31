
"""Write a Python program to calculate the sum of a list of numbers."""
def calculate_nums(list_of_nums):
    if len(list_of_nums) == 1:
        return list_of_nums[0]
    else:
        return list_of_nums[0] + calculate_nums(list_of_nums[1:])

print (calculate_nums([1, 5, 67, 1]))
print(sum([1, 5, 67, 1]))

"""Write a Python program to converting an Integer to a string in any base."""

def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))

# Write a Python program of recursion list sum. Go to the editor
# Test Data : [1, 2, [3,4], [5,6]]
# Expected Result : 21

def sum_of_lists(x):
    total = 0
    for item in x:
        if type(item) == list:
            total+=sum_of_lists(item)
        else:
            total += item
    return total

print (sum_of_lists([1, 2, [3,4], [5,6]]))

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print (factorial(4))

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(7))

# Write a Python program to get the sum of a non-negative integer.

def sum_of_ints(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_ints(int(n//10))

print (sum_of_ints(345))
cache = {}

def tro(item_to_calculate):
    x = []
    if item_to_calculate in cache:
        return cache[item_to_calculate]

    try:
        value = int(item_to_calculate)
    except:
        x.append(item_to_calculate)
    else:
        cache[item_to_calculate] = value
        print(value)
    print(x)

tro('trhfh')
