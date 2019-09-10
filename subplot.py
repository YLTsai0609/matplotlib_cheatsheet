from matplotlib import pyplot as plt
'''
create plot objrct
figure - container holiding our plot 
- think of that as a whole windows
axes - the actual plots
figure can have multiple plot
'''
'''
function-style to get current object
plt.gcf() # get current figure
plt.gca() # get current axis
BUT WE CAN USE Object-Style Programming to do it
'''

# print(plt.style.available)
# use style
plt.style.use('seaborn')

###### use cosmic style #######
# plt.xkcd()
# Once you chhose a style, 
# It might have some default color, linewidth, grid, or somthing else
# data
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
        56000, 62316, 64928, 67317, 68748,73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
         65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373,62375, 66674, 68745, 68746, 74583]         

# 可以丟進多個row和columns, default = 1
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
'''
使用print(ax)，來了解目前我們的plot物件狀態為何,
在nrows=2, ncols=1的情況下，產生一個list裡面有兩個axes
在nrows=2, ncols=2的情況下，產生一個list，裡面有兩個list,
兩個list各有兩個plot 
'''
 # DEFAULT linewidth = 1
ax2.plot(age_x, py_dev_y, linewidth=3, label='Python Devs')
ax2.plot(age_x, js_dev_y, linewidth=3,  label='JavaScript Devs')
 # 最後畫dot的圖形可以避免被遮住
ax1.plot(age_x, dev_y, linestyle='--', label='All Devs')
ax1.legend()
# 不知為什麼，但是就是這樣，xlabel, ylabel, title, 再換乘物件時要使用set_
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')
ax1.set_title('Median Salary (USD) by Age')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.grid(True)
plt.tight_layout()
# # ax.savefig('comic_style.png')
plt.show()


'''
subplot with 
fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=2,figsize=(12,10))
'''