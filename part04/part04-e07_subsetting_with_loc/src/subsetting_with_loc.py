#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    return  pd.read_csv('src/municipal.tsv', sep='\t', index_col='Region 2018').loc['Akaa':'Äänekoski',
        ['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %',]]

def main():
    return print(subsetting_with_loc())

if __name__ == "__main__":
    main()
