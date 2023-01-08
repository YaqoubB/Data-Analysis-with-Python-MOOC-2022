#!/usr/bin/env python3

def detect_ranges(L):
    l1 = sorted(L)
    l2 = []
    count = 0
    i = 1
    start = l1[i-1]
    while i < len(l1):
        if l1[i-1]+1 == l1[i]:
            count += 1
        else:
            if count == 0:
                l2.append(start)
            else:
                l2.append((start,l1[i-1]+1))
            start = l1[i]
            count = 0
        i += 1
    if count == 0:
        l2.append(start)
    else:
        l2.append((start,l1[i-1]+1))
        
    return l2

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
