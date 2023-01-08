#!/usr/bin/env python3

def interleave(*lists):
    l1 = []
    for i in zip(*lists):
        for j in i:
            l1.append(j)
    return l1


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
