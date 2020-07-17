'''
===================================================
converting colormap to rgb and rgba
===================================================
EXPLANATION:
	1. pick num_colors N
	2. pick color_map you need @ https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
	3. enjoy!
INPUTS:
	xxxxxxxxxxxxxxx
OPTIONAL INPUT:
	xxxxxxxxxxxxxxx
OPTIONAL INPUT KEYWORD:
	xxxxxxxxxxxxxxx
OUTPUT:
	xxxxxxxxxxxxxxx
EXAMPLE:
	xxxxxxxxxxxxxxx
REVISION HISTORY:
	functionality1  date1 author1
	functionality2  date2 author2
'''


from matplotlib import pyplot as plt
import numpy as np
import cycler
from typing import Tuple


def colormap2rgb(num_colors: int, colormap: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    從colormap中拿到rgba以及rgb

    Args:
        num_colors (int): 需要的顏色數量
        colormap (str): 使用的colormap

    Returns:
        Tuple[list, list]: rgba以及rgb

    Examples:

    rgba_list, rgb_list = colormap2rgb(num_colors=3, colormap='Paired')
    for line_idx in range(len(rgba_list)):
        plt.plot([i for i in range(10)],
                [i * line_idx for i in range(10)],
                c=rgba_list[line_idx], label=f'line {line_idx}')
        plt.legend()
    plt.show()
    print(rgba_list)
    """
    func = getattr(plt.cm, colormap)
    rgba_color = func(np.linspace(0, 1, num_colors))
    rgb_color = (rgba_color[:, 0:3] * 255).astype(int)
    return rgba_color, rgb_color


rgba_list, rgb_list = colormap2rgb(num_colors=5, colormap='Paired')

for line_idx in range(len(rgba_list)):
    plt.plot([i for i in range(10)],
             [i * line_idx for i in range(10)],
             c=rgba_list[line_idx], label=f'line {line_idx}')
    plt.legend()
plt.show()
print(rgba_list)
