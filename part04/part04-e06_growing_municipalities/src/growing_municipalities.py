#!/usr/bin/env python3

import pandas as pd
import numpy as np

def growing_municipalities(df):
    val = (len(df[df['Population change from the previous year, %']> 0]) / len(df)) 
    return val 

def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t", index_col='Region 2018')['Akaa':'Äänekoski']
    return print(f'Proportion of growing municipalities: {growing_municipalities(data)*100:.1f}%')


if __name__ == "__main__":
    main()
