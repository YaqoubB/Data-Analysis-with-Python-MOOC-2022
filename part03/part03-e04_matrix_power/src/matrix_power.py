#!/usr/bin/env python3

import numpy as np
import functools


def matrix_power(a, n):
    c, m = abs(n), a.shape[0]

    if n == 0:
        return np.eye(m)
    elif n < 0:
        a = np.linalg.inv(a)
        
    input = np.full((c, m, m), fill_value=a)
    return functools.reduce(lambda x,y: x@y, input)

def main():
    return

if __name__ == "__main__":
    main()
    s=np.array([[1, 6, 7],
    [7, 8, 1],
    [5, 9, 8]])
    a=np.array([[1,2], [3,4]])
    print(matrix_power(a, 2))


