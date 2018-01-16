"""
Non useful basic memory profiler function
"""
from memory_profiler import profile
import numpy as np
import time

precision = 4


@profile(precision=precision)
def some_math(n=100000):
    """ Defines a List expression that appends to list and calculates mean and standard deviation"""

    numbers = [i * i for i in range(0, n)]
    total = sum(numbers)
    #mean = total / len(numbers)
    mean = np.mean(numbers)
    std = np.std(numbers)
    print(f' Mean, std is {mean:0.3f} , {std:0.3f}')


@profile(precision=precision)
def some_math_with_generator(n=100000):
    """ Defines a Generator function to calculate mean and standard deviation"""
    numbers = (i * i for i in range(0, n))

    # Find mean
    total = 0
    for count, num in enumerate(numbers, 1):
        total += num
    mean = total / count

    # Find standard deviation
    numbers = (i * i for i in range(0, n))
    deviation = 0
    for count, num in enumerate(numbers, 1):
        deviation += (num - mean)** 2
    std = np.sqrt(deviation / count)

    print(f' Mean, std is {mean:0.3f} , {std:0.3f}')


if __name__ == '__main__':
    some_math()
    some_math_with_generator()
