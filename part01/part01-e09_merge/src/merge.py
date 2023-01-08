#!/usr/bin/env python3

def merge(L1, L2):
    L3 = []
    i = 0
    j = 0
    while i < len(L1):
        if L1[i] > L2[j]:
            L3.append(L2[j])
            j += 1
            if j == len(L2):
                L3.extend(L1[i:])
                break
        else:
            L3.append(L1[i])
            i += 1
            if i == len(L1):
                L3.extend(L2[j:])
                break
    return L3

def main(L1,L2):
    return merge(L1, L2)

if __name__ == "__main__":
    L1 = [1, 2, 3, 4, 5]
    L2 = [2, 3, 4, 5, 6]
    print(main(L1,L2))
