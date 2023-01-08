#!/usr/bin/env python3

import pandas as pd
import numpy as np

def split_date():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    data.dropna(how='all', axis=1, inplace=True)
    data.dropna(how='all', axis=0, inplace=True)
    dat = data['Päivämäärä'].str.split(expand=True)
    dat.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    dat['Hour'] = dat['Hour'].str.split(':', expand=True)[0]
    dat.replace({'Weekday' : {'ma':'Mon', 'ti':'Tue', 'ke':'Wed', 'to':'Thu', 'pe':'Fri', 'la':'Sat', 'su':'Sun'},}, inplace=True)
    dat.replace({'Month' : {'tammi':1, 'helmi':2, 'maalis':3, 'huhti':4, 'touko':5, 'kesä':6, 'heinä':7,
                             'elo':8, 'syys':9, 'loka':10, 'marras':11, 'joulu':12}}, inplace=True)
    dat = dat.astype({'Day': 'int', 'Month': 'int', 'Year': 'int', 'Hour': 'int'})
    return dat

def main():
    return print(split_date())
       
if __name__ == "__main__":
    main()
