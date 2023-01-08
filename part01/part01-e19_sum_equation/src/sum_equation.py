#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    s = sum(L)
    return " + ".join(map(str, L)) + " = " + str(s)

def main():
    pass

if __name__ == "__main__":
    main()
