'''
https://stackoverflow.com/questions/7821518/matplotlib-save-plot-to-numpy-array
https://stackoverflow.com/questions/20051160/renderer-problems-using-matplotlib-from-within-a-script/35407794#35407794


img size 600, 450, 3, fix height = 480
dpi 200
    13, 7 -> 1400, 2600


'''
import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
############## important  pick a backend ############
import matplotlib
matplotlib.use('Agg')

x = np.arange(0, 2 * np.pi, 0.02)
y = np.sin(x)
y1 = np.sin(2 * x)
y2 = np.sin(3 * x)
# ym1 = np.ma.masked_where(y1 > 0.5, y1)
# ym2 = np.ma.masked_where(y2 < -0.5, y2)
img = cv2.imread('mexico.jpg')
img = imutils.resize(img, height=400)
img_w, img_h = img.shape[1], img.shape[0]
dpi = 200
with plt.style.context(['science', 'no-latex', 'grid']):
    fig, ax = plt.subplots(figsize=((img_w) / dpi, img_h / dpi), dpi=dpi)
    ax.plot(x, y, label='sin x', color='red', linewidth=4)
    ax.plot(x, y1, label='sin 2x', color='green', linewidth=2)
    ax.plot(x, y2, label='sin 3x', color='orange', linewidth=10)
    plt.title('line demo')
    plt.legend(loc='upper right')
    plt.xticks(np.arange(8), ('Tom', 'Dick', 'Harry',
                              'Sally', 'Sue', 'PPP', 'QQQ', 'RRR'))
    ##################### convet to numpy array #############
    fig.canvas.draw()
    # Now we can save it to a numpy array.
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data_bgr = data.reshape(fig.canvas.get_width_height()[
        ::-1] + (3,))[..., ::-1]  # turn to bgr

    ##################### concat #########################
    print(img.shape)
    print(data_bgr.shape)
    # data_bgr = cv2.resize(data_bgr, (1280, 720))
    concat = np.concatenate([img, data_bgr], axis=0)
    cv2.imshow('concat images', concat)
    # cv2.imshow('shown by opencv', data_bgr)
    # cv2.imshow('img', img)
    cv2.waitKey(0)
