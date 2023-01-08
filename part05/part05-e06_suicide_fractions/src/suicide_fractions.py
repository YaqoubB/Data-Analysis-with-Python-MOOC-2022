#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    data = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    dat = data.groupby('country').apply(lambda x: (x['suicides_no']/x['population']).mean())
    return dat

def main():
    return print(suicide_fractions())
 
if __name__ == "__main__":
    main()


