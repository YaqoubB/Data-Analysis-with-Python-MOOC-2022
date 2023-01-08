#!/usr/bin/env python3

import pandas as pd

def suicide_fractions(data):
    dat = data.groupby('country').apply(lambda x: (x['suicides_no']/x['population']).mean())
    return dat
    
def suicide_weather():
    data = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    web = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col='Country', header=0)[0].squeeze()
    web = web.apply(lambda x: float(x.replace("\u2212", "-")))
    dat = suicide_fractions(data)
    cor = web.corr(dat, method='spearman')
    idx1, idx2 = web.index, dat.index
    common = idx1.intersection(idx2)
    return (len(dat), len(web), len(common), cor)

def main():
    (suicide_rows, temperature_rows, common_rows, spearman_correlation) = suicide_weather()
    print(f'Suicide DataFrame has {suicide_rows} rows')
    print(f'Temperature DataFrame has {temperature_rows} rows')
    print(f'Common DataFrame has {common_rows} rows')
    print(f'Spearman correlation: {spearman_correlation}')
    return 

if __name__ == "__main__":
    main()

