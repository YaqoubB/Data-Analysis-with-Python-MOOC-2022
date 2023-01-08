#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return (r1,r2)


def main():
    pass

if __name__ == "__main__":
    main()
