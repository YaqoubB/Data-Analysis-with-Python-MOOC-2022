#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    count = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            if count == 0:
                count += 1
                continue
            a,b,c,d = re.search(r'(\d+)\s+(\d+)\s+(\d+)[\t*|/s*]*(.*)', line).groups()
            print(f'{a}\t{b}\t{c}\t{(d).strip()}')
            result.append(f'{a}\t{b}\t{c}\t{(d).strip()}')
    return result


def main():
    pass

if __name__ == "__main__":
    main()
    red_green_blue(filename="src/rgb.txt")
    #255 250 250		snow
    #'255\t250\t250\tsnow'
