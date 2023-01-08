#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    val = data['Snow depth (cm)'].max()
    return val

def main():
    val = snow_depth()
    return print(f'Max snow depth: {val:.1f}')
if __name__ == "__main__":
    main()
