#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, "r") as my_file:
        for line in my_file:
            size, month, day, time, filename = re.search(r'(\d+) ([A-Z][a-z]+)\s+(\d{1,2}) (\d\d:\d\d) (.+)', line).groups()
            result.append((int(size), month, int(day), int(time[0:2]), int(time[3:]), filename))
    return result

def main():
    pass

if __name__ == "__main__":
    main()
    file_listing(filename="src/listing.txt")
    #-rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py
