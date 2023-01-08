#!/usr/bin/env python3

import pandas as pd

def cyclists():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    data.dropna(how='all', axis=1, inplace=True)
    data.dropna(how='all', axis=0, inplace=True)
    return data

def main():
    return cyclists()
    
if __name__ == "__main__":
    main()
