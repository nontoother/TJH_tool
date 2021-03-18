"""
Usage: used to make the file into right directory for tracking
owner: Tu Jiahan
Date: 2020-09-28
"""

import os
import shutil

PATH = 'E:/dataset/tracking_labelled'
IMG_PATH = 'E:/work/SiamFC/siamfc-tensorflow/__Data/tracking/Data/VID/train/tracking_train_0000'
ANNOTATION_PATH = 'E:/work/SiamFC/siamfc-tensorflow/__Data/tracking/Annotations/VID/train/tracking_train_0000'
for root, dirs, files in os.walk(PATH):
    for file in files:
        if file.endswith('jpg'):
            filename = file.split('.')[0]
            file_dir = filename[:12]
            save_path = os.path.join(IMG_PATH, file_dir)
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            shutil.copy(os.path.join(root, file), save_path)
        if file.endswith('xml'):
            filename = file.split('.')[0]
            file_dir = filename[:12]
            save_path = os.path.join(ANNOTATION_PATH, file_dir)
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            shutil.copy(os.path.join(root, file), save_path)