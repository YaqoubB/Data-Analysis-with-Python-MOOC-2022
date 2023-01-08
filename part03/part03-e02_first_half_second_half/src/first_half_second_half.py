#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    n, m = np.shape(a) 
    x1 = np.sum(a[:,0:m//2], axis=1)
    x2 = np.sum(a[:,m//2:], axis=1)
    return a[x1>x2]

def main():
    pass

if __name__ == "__main__":
    main()
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
    print(first_half_second_half(a))



