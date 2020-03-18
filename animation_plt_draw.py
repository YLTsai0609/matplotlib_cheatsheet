import numpy as np
import matplotlib.pyplot as plt
x = np.arange(50)
y = np.sin(x)

# fig, ax = plt.subplots(figsize=(15, 5))
# ax.scatter(x, y)

plt.ion()
plt.show()
for i in range(50):
    plt.scatter(x[i], y[i], c='b', alpha=.6)
    # erease the past
    if i > 0:
        plt.scatter(x[i-1], y[i-1], c='white', edgecolors='white')
    plt.title(f'Iteration {i}')
    plt.draw()
    plt.pause(0.3)
