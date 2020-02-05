import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# 單一向量
# (x, y, vx, vy) angles, scale_units, scale
plt.quiver(0,0,0,0.01, color='black', angles="xy", scale_units='xy', scale=1)
plt.title('Single vector')
plt.show()

# 常數向量場

x2 = np.array([0])
y2 = np.array([0])
v = np.array([1])
u = np.array([5])
fig, ax = plt.subplots()
q = ax.quiver(x2,y2,u,v, units='xy')
plt.title('Contant vector field')
plt.show()

# 變數向量場


x,y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .2))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)
fig, ax = plt.subplots()
q = ax.quiver(x,y,u,v)
plt.title('Variable vector filed')
plt.show()


# 單一向量 on polar plane
fig= plt.figure()
ax = fig.add_subplot(111, projection='polar')

# ax.set_rticks([])
# ax.set_rmin(0)
# ax.set_rmax(1)

ax.arrow(45/180.*np.pi, 0.1, 0, 0.4, alpha = 0.5, width = 0.05,
                 edgecolor = 'black', facecolor = 'green', lw = 1, zorder = 5)

plt.title('Single vector on polar system')
plt.show()

# for loop 加上向量 on polar plane
df = pd.read_csv('three_face.csv')
resource = [df.iloc[0], df.iloc[1], df.iloc[2]]

anchor_face = resource[0][1:]
compare_face = resource[1][1:]
diff = compare_face - anchor_face
rgb_values = sns.color_palette("Set2", len(anchor_face))

fig= plt.figure()
ax = fig.add_subplot(111, projection='polar')

for idx in range(68):
    # the anchor face
    ax.scatter(anchor_face[2 * idx + 1], # theta
               anchor_face[2 * idx], # radius
               color=rgb_values[0]
              )
    
    ax.scatter(compare_face[2 * idx + 1], # theta
           compare_face[2 * idx], # radius
           color=rgb_values[1]
          )

    # difference vector
    # (theta, r, d theta, dr)
    # (透明度, 箭頭尾, 箭頭頭)
    ax.arrow(anchor_face[2 * idx + 1], # theta
             anchor_face[2 * idx], # radius
             diff[2 * idx + 1], # d theta,
             diff[2 * idx], # dr,
             alpha = 0.5, width = 0.005, head_width = 0.05,
                     edgecolor = 'black', lw = 1, zorder = 5)

# ax.set_rticks([])
ax.set_ylim([0,0.7]) # the r range
ax.set_theta_direction(-1) # y-axis downside
plt.title('Two face difference')
plt.show()

