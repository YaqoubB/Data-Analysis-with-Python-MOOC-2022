#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cleaning_data():
    data = pd.read_csv('src/presidents.tsv', sep='\t')
    data['President'] = data['President'].apply(lambda x: ' '.join(x.split(', ')[::-1]))
    data['Vice-president'] = data['Vice-president'].apply(lambda x: ' '.join(x.split(', ')[::-1]).title())
    data['Start'] = data['Start'].apply(lambda x: x.split(' ')[0]).astype(int)
    data['Last'] = pd.to_numeric(data['Last'], errors='coerce')
    data['Seasons'] = data['Seasons'].replace(to_replace='two', value=2).astype(int)
    return data

def main():
    return cleaning_data()

if __name__ == "__main__":
    main()
