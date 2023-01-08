#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    n,m = a.shape
    L = []
    for i in a:
        L.append(i.reshape(1,m))
    return L

def get_column_vectors(a):
    n,m = a.shape
    L = []
    for i in a.T:
        L.append(i.reshape(n,1))
    return L

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
