#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    dat = df['Päivämäärä'].str.split(expand=True)
    dat.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    dat['Hour'] = dat['Hour'].str.split(':', expand=True)[0]
    dat.replace({'Weekday' : {'ma':'Mon', 'ti':'Tue', 'ke':'Wed', 'to':'Thu', 'pe':'Fri', 'la':'Sat', 'su':'Sun'},}, inplace=True)
    dat.replace({'Month' : {'tammi':1, 'helmi':2, 'maalis':3, 'huhti':4, 'touko':5, 'kesä':6, 'heinä':7,
                             'elo':8, 'syys':9, 'loka':10, 'marras':11, 'joulu':12}}, inplace=True)
    dat = dat.astype({'Day': 'int', 'Month': 'int', 'Year': 'int', 'Hour': 'int'})
    return dat


def cycling_weather():
    data1 = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';').dropna(how='all', axis=1).dropna(how='all', axis=0)
    data2 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    dat1 = split_date(data1)
    dat1 = pd.concat([dat1, data1.iloc[:, 1:]], axis=1)
    dat = pd.merge(dat1, data2, left_on=['Day', 'Month', 'Year'], right_on=['d', 'm', 'Year'], how='inner')
    dat = dat.drop(['d', 'm', 'Time', 'Time zone'], axis=1)
    return dat

def main():
    return print(cycling_weather())

if __name__ == "__main__":
    main()
