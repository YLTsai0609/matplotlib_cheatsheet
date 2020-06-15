from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# show the default style
# print(plt.style.available)
# use style

plt.style.use('seaborn')
# use science 
# plt.style.context(['science', 'ieee','no-latex'])
x = 5.5 * np.random.randn(20,1) + 25
y = 5.5 * np.random.randn(20,1) + 25
# s -> size, c -> green, makers = 'X'
# edgecolor='black', linewidth= 2
# alpha = .7
# default color 是灰階, 可以透過cmaps = 'Blues', 'Greens' to fix

'''
COLOR PART
color = 5.5 * np.random.randn(20,1) + 25
plt.scatter(x, y, s=100, c=color, cmap='Blues','summer'
            edgecolors='black', linewidths=2,
            alpha=.75)
# 需要加入color bar
cbar = plt.colorbar()
cbar.set_label('Earns More Money')
''';
'''
Size PART
(1)
without legend
'''
# size = 5.5 * np.random.randn(20,1) + 200
# color = 5.5 * np.random.randn(20,1) + 25
# ax = plt.scatter(x, y, s=size, c=color, cmap='Blues',
#             edgecolors='black', linewidths=2,
#             alpha=.75)

# Size plot with legend
N = 50
M = 5 # Number of bins

x = np.random.rand(N)
y = np.random.rand(N)
a2 = 400*np.random.rand(N)

# Create the DataFrame from your randomised data and bin it using groupby.
df = pd.DataFrame(data=dict(x=x, y=y, a2=a2))
bins = np.linspace(df.a2.min(), df.a2.max(), M)
grouped = df.groupby(np.digitize(df.a2, bins))

# Create some sizes and some labels.
sizes = [50*(i+1.) for i in range(M)]
labels = ['Tiny', 'Small', 'Medium', 'Large', 'Huge']

for i, (name, group) in enumerate(grouped):
    plt.scatter(group.x, group.y, s=sizes[i], alpha=0.5, label=labels[i])

plt.legend()
plt.show()

# log scale if you want
# plt.tight_layout()
# plt.show()
