from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# show the default style
# print(plt.style.available)
# use style
plt.style.use('fivethirtyeight')
# print(dir(plt))
###### use cosmic style #######
# plt.xkcd()
# Once you chhose a style, 
# It might have some default color, linewidth, grid, or somthing else
# data
columns=['Age']
data = 5.5 * np.random.randn(100,1) + 25
df = pd.DataFrame(columns =columns, 
                  data = data)

# bins integer -> equally, list -> according list cut into bins
bins = [0, 10, 20,30,40,50,60,70]
median_age = df['Age'].median()
color='#fc4f30'
# log for frequency counts
plt.hist(df['Age'], bins=bins, edgecolor='black')

plt.axvline(median_age, color=color,
            label='Age Median', linewidth=2)

plt.title('Age')
plt.ylabel('Total Counts')
plt.legend()
# use plt.ticks
# plt.grid(True)
plt.tight_layout()
plt.show()