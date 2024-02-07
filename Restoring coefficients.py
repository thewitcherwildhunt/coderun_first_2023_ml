from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


def f(x, a, b, c):
    return (a * np.sin(x) + b * np.log(x)) ** 2 + c * x ** 2


def main():
    data = pd.read_csv('data.csv', header=None, names=['x', 'y'])
    print(curve_fit(f, data['x'], data['y'])[0])


main()
