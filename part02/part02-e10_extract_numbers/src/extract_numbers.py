#!/usr/bin/env python3

def extract_numbers(s):
    L = []
    for i in s.split():
        try:
            i = int(i)
        except ValueError:
            try:
                i = float(i)
            except ValueError:
                continue
            else:
                L.append(i)
        else:
            L.append(i)
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
