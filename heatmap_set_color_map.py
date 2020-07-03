import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# use those
# idx_list = pivot_df.index.tolist()
# col_list = pivot_df.columns.tolist()
# count_values = pivot_df.values

# Choosing Colormaps in Matplotlib
# https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html
# pick sequential colormap

# make annotation bigger

col_list = ["cucumber", "tomato", "lettuce", "asparagus",
            "potato", "wheat", "barley"]
idx_list = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
            "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

count_values = harvest
smoother_values_for_plot = 10 * (count_values ** (0.5))

bigger_annotation = {'font.size': 18}


with plt.rc_context(bigger_annotation):
    with plt.style.context(['science', 'no-latex']):
        # paper style =)
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
        im = ax.imshow(smoother_values_for_plot, cmap='Blues')

        # We want to show all ticks...
        ax.set_xticks(np.arange(len(col_list)))
        ax.set_yticks(np.arange(len(idx_list)))
        # ... and label them with the respective list entries
        ax.set_xticklabels(col_list)
        ax.set_yticklabels(idx_list)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(idx_list)):
            for j in range(len(col_list)):
                text = ax.text(j, i, count_values[i, j],
                               ha="center", va="center", color="w")

        ax.set_title("Figure Title")
        fig.tight_layout()
        plt.show()
