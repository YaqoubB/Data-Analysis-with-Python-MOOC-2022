#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as my_file:
        l_count = 0
        w_count = 0
        c_count = 0
        for line in my_file:
            c_count += len(line)
            l_count += 1
            line = line.split()
            w_count += len(line)

    return (l_count, w_count, c_count)

def main():
    for i in sys.argv[1:]:
        l_count, w_count, c_count = file_count(i)
        print(f'{l_count}\t{w_count}\t{c_count}\t{i}')

if __name__ == "__main__":
    main()
    #python src/file_count.py src/test.txt
