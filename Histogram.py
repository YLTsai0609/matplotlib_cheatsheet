from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# show the default style
# print(plt.style.available)
# use style
# plt.style.use('fivethirtyeight')
# print(dir(plt))
###### use cosmic style #######
# plt.xkcd()
# Once you chhose a style,
# It might have some default color, linewidth, grid, or somthing else
# data
columns = ['Age']
data = 5.5 * np.random.randn(100, 1) + 25
df = pd.DataFrame(columns=columns,
                  data=data)

df_sales = pd.DataFrame({
    'HUMIDITY': 100 * np.random.random(size=100)
})

# bins integer -> equally, list -> according list cut into bins
bins = [0, 10, 20, 30, 40, 50, 60, 70]
median_age = df['Age'].median()
color = '#fc4f30'
# log for frequency counts

with plt.style.context(['science', 'grid', 'no-latex']):
    plt.hist(df['Age'], bins=bins, edgecolor='green', label='Age')
    plt.axvline(median_age, color=color,
                label='Age Median', linewidth=2)

    plt.axvline(median_age, color=color,
                label='Age Median', linewidth=2)

    plt.title('Age')
    plt.ylabel('Total Counts')
    plt.legend()
    # use plt.ticks
    # plt.grid(True)
    plt.tight_layout()
    plt.show()

# a function
'''
col = 'HUMIDITY'
df = df_sales
offset = df[col].std() / 2

fig, ax = plt.subplots(figsize=(12,8))
bins = np.linspace(df[col].min() - offset, df[col].max() + offset, 20)

ax.hist(df[col], bins=bins, edgecolor='black')
plt.title(col)
plt.ylabel('total counts')
plt.legend()
plt.grid(True)
plt.tight_layout()

'''
