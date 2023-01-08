#!/usr/bin/env python3

import numpy as np

def diamond(n):
    I = np.eye(n, dtype=int)
    L = []
    for i in range(n):
        row = list(np.concatenate((I[i,:n], I[i,:-1][::-1])))
        L.append(row)
        
    L = L[1:][::-1] + L
    return np.asarray(L)

def main():
    pass

if __name__ == "__main__":
    main()
    print(diamond(3))
