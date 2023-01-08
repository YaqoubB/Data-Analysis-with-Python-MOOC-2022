#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    data = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x1, x2, x3, x4, x5, y = data['X1'], data['X2'], data['X3'], data['X4'], data['X5'], data['Y']
    X = pd.concat([x1, x2, x3, x4, x5], axis=1)
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f'Coefficient of X1 is {coefficients[0]}')
    print(f'Coefficient of X2 is {coefficients[1]}')
    print(f'Coefficient of X3 is {coefficients[2]}')
    print(f'Coefficient of X4 is {coefficients[3]}')
    print(f'Coefficient of X5 is {coefficients[4]}')
    
if __name__ == "__main__":
    main()
