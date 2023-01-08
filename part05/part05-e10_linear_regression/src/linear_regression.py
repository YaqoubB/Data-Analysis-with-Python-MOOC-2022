#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model=LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 2, 3, 4, 5])
    slope, intercept = fit_line(x,y)
    plt.plot(x, y,)
    plt.plot(x, intercept*x + slope)
    plt.show()
    print(f'Slope: {slope:.1f}')
    print(f'Intercept: {intercept:.11f}')

if __name__ == "__main__":
    main()



