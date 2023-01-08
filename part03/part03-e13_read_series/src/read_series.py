#!/usr/bin/env python3


import pandas as pd 

def read_series():
    res = pd.Series([])
    while 1:
        line = input()
        if line == "":
            break
        try:
            index, value = line.split()
            res[index] = value
        except:
            raise Exception
    return res

def main():
    pass

if __name__ == "__main__":
    main()
    read_series()