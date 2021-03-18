"""
Usage: Used for generating heat map through *.npy, at the same time add pure heat map to the source image.
        This .py will generate three pictures, heatmap.jpg is a heat map with color bar, heatmap_crop.jpg is a pure heat map picture, heat_map.jpg is adding pure heat map to the source image
owner: Tu Jiahan
Date: 2020-09-16
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import cv2

sns.set()

heat_map = np.load('infrared.npy')
pd.DataFrame(heat_map)
f, ax = plt.subplots(figsize=(19.2, 10.8))
plt.axis('off')
sns.heatmap(heat_map, ax=ax)
plt.savefig("heatmap.jpg")
img = cv2.imread('heatmap.jpg')
img_crop = img[130:960, 240:1430]
img_crop = cv2.resize(img_crop, (1920, 1080))
src_img = cv2.imread('E:/gitlab/video_filter/src_img.jpg')
cv2.imshow('img', img_crop)
cv2.waitKey(-1)
cv2.imwrite('heatmap_crop.jpg', img_crop)
alpha = 0.65
img_add = cv2.addWeighted(img_crop, alpha, src_img, 1 - alpha, 0)
cv2.imwrite('heat_map2.jpg', img_add)
cv2.imshow('imgadd', img_add)
cv2.waitKey(-1)
cv2.destroyAllWindows()