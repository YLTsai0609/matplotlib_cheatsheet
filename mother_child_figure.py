# https://stackoverflow.com/questions/58954835/how-to-change-matplotlib-settings-temporarily


from matplotlib import pyplot as plt
import numpy as np

# Generate the main data
X = np.linspace(-6, 6, 1024)
Y = np.sinc(X)

# Generate data for the zoomed portion
X_detail = np.linspace(-3, 3, 1024)
Y_detail = np.sinc(X_detail)


rc1 = {"font.size": 16}
rc2 = {"font.size": 8}

plt.rcParams.update(rc1)

with plt.style.context(['science', 'grid', 'no-latex']):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
    ax.plot(X, Y, label='prediction')
    ax.plot(X, [0.03 for i in range(X.shape[0])], label='baseline')

    with plt.rc_context(rc2):
        axins = ax.inset_axes([0.6, 0.6, 0.37, 0.37])
        axins.plot(X_detail, Y_detail)

plt.show()
