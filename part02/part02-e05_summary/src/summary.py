#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    l = []
    count = 0
    sum = 0
    val = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            try:
                line = line.strip()
                sum += float(line)
                l.append(float(line))
                count += 1
            except ValueError:
                pass

    average = sum / count
    for i in l:
        val += (i - average) ** 2
    sd = sqrt(val / (count-1))
    return sum, average, sd

def main():
    filename=sys.argv[1:]
    for i in filename:
        sum, average, sd = summary(i)
        print(f'File: {i} Sum: {sum:6f} Average: {average:6f} Stddev: {sd:6f}')

if __name__ == "__main__":
    main()
    #python src/summary.py src/example.txt src/example2.txt src/example3.txt

