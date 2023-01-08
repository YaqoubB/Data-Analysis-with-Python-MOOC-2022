#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date(df):
    dat = df['Päivämäärä'].str.split(expand=True)
    dat.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    dat['Hour'] = dat['Hour'].str.split(':', expand=True)[0]
    dat.replace({'Weekday' : {'ma':'Mon', 'ti':'Tue', 'ke':'Wed', 'to':'Thu', 'pe':'Fri', 'la':'Sat', 'su':'Sun'},}, inplace=True)
    dat.replace({'Month' : {'tammi':1, 'helmi':2, 'maalis':3, 'huhti':4, 'touko':5, 'kesä':6, 'heinä':7,
                             'elo':8, 'syys':9, 'loka':10, 'marras':11, 'joulu':12}}, inplace=True)
    dat = dat.astype({'Day': 'int', 'Month': 'int', 'Year': 'int', 'Hour': 'int'})
    return dat


def cyclists_per_day():
    data1 = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';').dropna(how='all', axis=1).dropna(how='all', axis=0)
    dat1 = split_date(data1)
    dat1 = pd.concat([dat1, data1.iloc[:, 1:]], axis=1)
    dat1 = dat1.drop(['Weekday', 'Hour'], axis=1)
    dat1 = dat1.groupby(['Year', 'Month','Day']).sum()
    return dat1
    
def main():
    res = cyclists_per_day()
    res = res.loc[(2017, 8),:]
    res.plot()
    plt.show()
    return 

if __name__ == "__main__":
    main()


