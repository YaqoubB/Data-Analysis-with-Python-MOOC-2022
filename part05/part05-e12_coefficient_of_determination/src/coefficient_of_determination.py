#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    data = pd.read_csv("src/mystery_data.tsv", sep="\t")
    x1, x2, x3, x4, x5, y = data['X1'], data['X2'], data['X3'], data['X4'], data['X5'], data['Y']
    X = pd.concat([x1, x2, x3, x4, x5], axis=1)
    x1, x2, x3, x4, x5 = x1.values.reshape(-1, 1), x2.values.reshape(-1, 1), x3.values.reshape(-1, 1), x4.values.reshape(-1, 1), x5.values.reshape(-1, 1)
    model_X = linear_model.LinearRegression(fit_intercept=True).fit(X, y).score(X, y)
    model_x1 = linear_model.LinearRegression(fit_intercept=True).fit(x1, y).score(x1, y)
    model_x2 = linear_model.LinearRegression(fit_intercept=True).fit(x2, y).score(x2, y)
    model_x3 = linear_model.LinearRegression(fit_intercept=True).fit(x3, y).score(x3, y)
    model_x4 = linear_model.LinearRegression(fit_intercept=True).fit(x4, y).score(x4, y)
    model_x5 = linear_model.LinearRegression(fit_intercept=True).fit(x5, y).score(x5, y)
    r_list = [model_X, model_x1, model_x2, model_x3, model_x4, model_x5]
    return r_list
    
def main():
    R2 = coefficient_of_determination()
    print(f'R2-score with feature(s) X: {R2[0]:.4f}')
    for i, r in enumerate(R2[1:]):
        print(f'R2-score with feature(s) X{i+1}: {r:.4f}')

if __name__ == "__main__":
    main()