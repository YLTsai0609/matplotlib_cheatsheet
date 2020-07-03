# https://stackoverflow.com/questions/58954835/how-to-change-matplotlib-settings-temporarily


from matplotlib import pyplot as plt

rc1 = {"font.size" : 16}
rc2 = {"font.size" : 8}

plt.rcParams.update(rc1)

fig, ax = plt.subplots(nrows=1, ncols=1)

with plt.rc_context(rc2):
    axins = ax.inset_axes([0.6, 0.6, 0.37, 0.37])

plt.show()
