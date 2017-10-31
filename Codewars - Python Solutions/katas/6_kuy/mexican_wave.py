"""
Example

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""

def wave(str):
    # Code here
    return ["".join([str[:i],str[i].upper(), str[i+1:]]) for i in range(len(str)) if str[i].isalpha()]