from matplotlib import pyplot as plt
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
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


# DEFAULT linewidth = 1
plt.plot(age_x, py_dev_y, linewidth=3, label='Python Devs')
plt.plot(age_x, js_dev_y, linewidth=3, label='JavaScript Devs')
# 最後畫dot的圖形可以避免被遮住
plt.plot(age_x, dev_y, linestyle='--', label='All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.savefig('comic_style.png')
plt.show()
