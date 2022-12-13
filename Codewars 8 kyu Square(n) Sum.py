# 8 kyu Square(n) Sum
'''
DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
'''
import numpy as np
def square_sum(numbers):
    return np.sum(np.square(numbers))