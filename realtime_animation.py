import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    # data = pd.read_csv('data.csv')
    data = pd.DataFrame({
        'x_value': [i for i in range(10000)],
        'total_1': [5 * i for i in range(10000)],
        'total_2': [3 * i + 2 for i in range(10000)],
    })
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.tight_layout()
plt.show()
