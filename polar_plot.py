import numpy as np
import cv2
from imutils import face_utils
import dlib
import numba as nb
import pandas as pd
import cv2
import os
from math import atan2, atan
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

project_path_your_computer = '/Users/longlong/Desktop/face_clustering'

landmark_model_path = os.path.join(project_path_your_computer,'contributed/Project_FaceClustering/models/shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(landmark_model_path)

save_path = os.path.join(project_path_your_computer, 'contributed/Project_FaceClustering/data/unalign_csv_fifteenPeople_per_one_image.csv')
df_fts = pd.read_csv(save_path)
df_fts





ft_names = []
for i in range(68):
    ft_names.extend([f'nomorlized_r_{i}', f'theta_{i}'])


# +
all_file = df_fts['file_parh'].tolist()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
rgb_values = sns.color_palette("Set2", len(all_file))
# rgb_values = sns.color_palette("hls", len(all_file))
# board = np.full((160, 160, 3), fill_value=255)

for img_idx, f_name in enumerate(all_file[:1]):
    ft_series = df_fts.iloc[img_idx][ft_names]
    for ft_idx in range(68):
        # 只有一開始要加上legend, 之後就不用
        if ft_idx == 0:
            ax.scatter(ft_series[2 * ft_idx + 1], # theta
               ft_series[2 * ft_idx ], # radius
               color=rgb_values[img_idx],
               label = img_idx)
        else:
            ax.scatter(ft_series[2 * ft_idx + 1], # theta
           ft_series[2 * ft_idx ], # radius
           color=rgb_values[img_idx])



ax.set_theta_direction(-1) # y-axis downside
plt.legend()
plt.show()
# ax.set_yticklabels([])

# ax.spines['polar'].set_visible(False)
# ax.set_theta_zero_location("W")
# -

