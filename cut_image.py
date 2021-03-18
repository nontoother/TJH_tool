"""
Usage: Draw a specific rectangle on the image to see if the rectangle is good.
owner: Tu Jiahan
Date: 2020-09-14
"""

import cv2
import os
src_path = 'E:/gitlab/video_filter/rect/'
save_path = 'E:/gitlab/video_filter/rect/'

for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith('jpg'):
            tmp_path = os.path.join(root, file)
            img = cv2.imread(tmp_path)
            print(len(img), len(img[0]), len(img[0][0]))
            print(img.shape)
            cv2.rectangle(img, (117, 172), (887, 783), (0, 0, 255), 2)
            cv2.imshow('img', img)
            cv2.waitKey(-1)
            path = os.path.join(save_path, 'rect2.jpg')
            cv2.imwrite(path, img)
            cv2.destroyAllWindows()