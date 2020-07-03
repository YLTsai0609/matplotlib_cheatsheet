# -*- coding: utf-8 -*-
# # Color code
# * [hex color code, rgb, hsv](https://htmlcolorcodes.com/)

from matplotlib import pyplot as plt
import numpy as np
# show the default style
# print(plt.style.available)
# use style

# plt.style.use('fivethirtyeight')

# print(dir(plt))
###### use cosmic style #######
# plt.xkcd()
# Once you choose a style, 
# It might have some default color, linewidth, grid, or somthing else
# data
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(age_x))
width = 0.25
dev_y = [38496, 42000, 46752, 49320, 53200,
        56000, 62316, 64928, 67317, 68748,73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
         65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373,62375, 66674, 68745, 68746, 74583]         


# Use plt.bar instead of plt.plot, just simple
# plt.bar(age_x, dev_y, label='All Devs')
## if you want to plot bar with line 
# just plt.bar with plt.plot
# plt.plot(age_x, py_dev_y,color='green', linewidth=3, label='Python Devs')
################ REAL barplot ################
# a little hacky

with plt.style.context(['science','no-latex']):
    plt.bar(x_indexes, py_dev_y, width = width, label='Python Devs')
    plt.bar(x_indexes - width, dev_y, width=width, label='All Devs')
    plt.bar(x_indexes + width, js_dev_y,width = width,  label='JavaScript Devs')
    # 最後畫dot的圖形可以避免被遮住

    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by Age')
    plt.legend()
    # use plt.ticks
    plt.xticks(ticks=x_indexes, labels=age_x)
    # plt.grid(True)
    plt.tight_layout()
    # plt.savefig('comic_style.png')
    plt.show()
