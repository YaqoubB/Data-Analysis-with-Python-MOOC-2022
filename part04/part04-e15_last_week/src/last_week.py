
#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    file = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    data = file.copy()

    data['LW'] = pd.to_numeric(data['LW'], errors='coerce')

    data['Peak Pos'] = np.nan
    data.loc[(data['LW'] == file['Peak Pos']), ['Peak Pos']] = file['Peak Pos']
    data.loc[(data['LW'] != file['Peak Pos']) & (data['Pos'] != file['Peak Pos']), ['Peak Pos']] = file['Peak Pos']

    data.loc[(file['LW'] == 'New') | (file['LW'] == 'Re'), data.columns] = np.nan

    data['Pos'] = data['LW']
    data['LW'] = np.nan
    data['WoC'] -= 1

    indx = set(range(1, len(data)+1))
    d = set(data['Pos'].dropna())
    data.loc[pd.isnull(data['Pos']), ['Pos']] = sorted(list(indx - d))

    data = data.sort_values(by=['Pos'])

    return data

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
