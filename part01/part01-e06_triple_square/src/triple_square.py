#!/usr/bin/env python3

def triple(x):
    return x*3

def square(x):
    return x**2

def main():
    for i in range(1,11):
        a = triple(i)
        b = square(i)
        if a < b:
            break
        print(f'triple({i})=={a} square({i})=={b}')

if __name__ == "__main__":
    main()
