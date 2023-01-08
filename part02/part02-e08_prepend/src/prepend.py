#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, string: str):
        self.start = string

    def write(self, s:str):
        print(self.start + s)

def main():
    pass

if __name__ == "__main__":
    main()
    p = Prepend("+++ ")
    p.write("Hello")
