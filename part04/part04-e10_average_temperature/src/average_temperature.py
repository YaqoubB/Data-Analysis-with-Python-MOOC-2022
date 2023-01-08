#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    val = data[data['m'] == 7]['Air temperature (degC)'].mean()
    return val

def main():
    val = average_temperature()
    return print(f'Average temperature in July: {val:.1f}')

if __name__ == "__main__":
    main()
