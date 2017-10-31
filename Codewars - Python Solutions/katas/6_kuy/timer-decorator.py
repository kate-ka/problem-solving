import time



def timer(limit):
    """decorator that validates if a
    function it decorates is executed within (less than)
    a given seconds interval and returns a
    boolean True or False accordingly.
"""

    def count_limit(func):
        def inner(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            return end - start < limit

        return inner

    return count_limit