#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    data = pd.read_csv("src/municipal.tsv", sep="\t", index_col='Region 2018')
    data = data['Akaa':'Äänekoski']
    label_swe = 'Share of Swedish-speakers of the population, %'
    label_foreign = 'Share of foreign citizens of the population, %'
    swe, foreign  = data[label_swe], data[label_foreign]
    res = data[(swe > 5) & (foreign > 5)]
    return res[['Population', label_swe, label_foreign]]

def main():
    return swedish_and_foreigners()

if __name__ == "__main__":
    main()


def some():
    return print('hello')

some()