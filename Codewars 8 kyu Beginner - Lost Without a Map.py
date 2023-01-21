#8 kyu Beginner - Lost Without a Map
'''
DESCRIPTION:
Given an array of integers, return a new array with each value doubled.

For example:
[1, 2, 3] --> [2, 4, 6]
'''
def maps(a):
    result = 2
    new = []
    for x in a:
        result = x*2
        new.append(result)
    return new