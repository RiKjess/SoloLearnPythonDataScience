"""
Multiples of 3 & 5


You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.
"""

import numpy as np

arr = np.arange(1,101)

print("Array:", arr)

print("Array of numbers below 100 that are multiples of both 3 and 5:", arr[(arr%3==0) & (arr%5==0) & (arr<100)])

