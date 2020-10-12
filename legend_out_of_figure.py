'''
https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
ax.plot return a tuple
get Line2D objects
legend object
https://matplotlib.org/api/legend_api.html#matplotlib.legend.Legend
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.02)
y = np.sin(x)
y1 = np.sin(2 * x)
y2 = np.sin(3 * x)
# ym1 = np.ma.masked_where(y1 > 0.5, y1)
# ym2 = np.ma.masked_where(y2 < -0.5, y2)
with plt.style.context(['science', 'no-latex']):
    fig, ax = plt.subplots(figsize=(3, 2), dpi=200)
    p1, = ax.plot(x, y, label='sin x', color='red', linewidth=4)

    p2, = ax.plot(x, y1, label='sin 2x', color='green', linewidth=2)
    p3, = ax.plot(x, y2, label='sin 3x', color='orange', linewidth=2)
    p4 = ax.axvline(x=1, label='focus line', color='gray',
                    linestyle='-', linewidth=2)
    plt.legend(handles=[p1, p2, p3, p4], title='Legends', bbox_to_anchor=(
        1.01, 1), loc='upper left', fontsize='xx-small')
    plt.title('line demo')
    # plt.legend(loc='upper right')
    plt.tight_layout()
    plt.xticks(np.arange(8), ('Tom', 'Dick', 'Harry',
                              'Sally', 'Sue', 'PPP', 'QQQ', 'RRR'))
    plt.show()
