'''
saving png too slow
if we want to combine video with matplotlib
we need more faster way
https://stackoverflow.com/questions/8598673/how-to-save-a-pylab-figure-into-in-memory-file-which-can-be-read-into-pil-image/8598881

the backend setting
https://matplotlib.org/tutorials/introductory/usage.html#backends

AGG dpi 200, saving 1 fps
# '''


from PIL import Image
import numpy as np
import io
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
from time import time
import matplotlib.style as mplstyle

matplotlib.use('Agg')  # set backend for plt.figure to np.array
mplstyle.use(['science', 'grid', 'no-latex', 'fast'])  # probably faser
plt.ioff()  # turn off the interactive mode to speed up the figure to np.array


treatment = []
control = []
n_exp = 50
for _ in range(n_exp):
    start = time()
    plt.figure()
    plt.plot([1, 2])
    plt.title("test")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    im = Image.open(buf)
    im_arr = np.array(im)
    buf.close()
    plt.close('all')
    # print(im_arr.shape)
    treatment.append(time() - start)
    ############ control ##########
    start = time()
    fig, ax = plt.subplots()
    plt.plot([1, 2])
    plt.title("test")
    fig.canvas.draw()
    # Now we can save it to a numpy array.
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data_bgr = data.reshape(fig.canvas.get_width_height()[
        ::-1] + (3,))[..., ::-1]  # turn to bgr
    plt.close('all')
    control.append(time() - start)
print('treatment : ', np.mean(np.array(treatment)))
print('control : ', np.mean(np.array(control)))
im.show()
