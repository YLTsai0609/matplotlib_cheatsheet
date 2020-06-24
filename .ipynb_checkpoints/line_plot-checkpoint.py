import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.02) # 
y = np.sin(x)
y1 = np.sin(2*x)
y2 = np.sin(3*x)
# ym1 = np.ma.masked_where(y1 > 0.5, y1)
# ym2 = np.ma.masked_where(y2 < -0.5, y2)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y,label='sin x',color='red', linewidth=4)
ax.plot(x, y1,label='sin 2x',color='green', linewidth=2)
ax.plot(x, y2,label='sin 3x',color='orange', linewidth=10)
plt.title('line demo')
plt.legend(loc='upper right')
plt.xticks(np.arange(8), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue','PPP','QQQ','RRR','SSS'))
plt.show()


