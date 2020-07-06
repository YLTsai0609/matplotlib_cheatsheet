import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# plt.style.use('fivethirtyeight')

array = np.random.uniform(low=5, high=50, size=10)

array_sorted = pd.Series(array).sort_values(ascending=False).values[::-1]


show_columns = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J"]
show_columns.reverse()

with plt.style.context(['science', 'grid', 'no-latex']):
    plt.barh(show_columns, array_sorted)
    plt.xlabel('Price')
    # No need, self document by category
    # plt.ylabel
    plt.title("Price vs ABCDE")
    plt.tight_layout()
    plt.show()
