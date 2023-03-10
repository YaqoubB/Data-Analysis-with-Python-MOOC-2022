#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(n)
    return np.outer(a,a)


def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
