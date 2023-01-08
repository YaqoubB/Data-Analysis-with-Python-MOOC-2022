#!/usr/bin/env python3

import pandas as pd

def below_zero():
    data = pd.read_csv('src/kumpula-weather-2017.csv')
    val = len(data[data['Air temperature (degC)'] < 0])
    return val

def main():
    val = below_zero()
    return print(f'Number of days below zero: {val}')
    
if __name__ == "__main__":
    main()
