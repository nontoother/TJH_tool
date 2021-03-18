"""
Usage: Used for checking which picture has the error "premature end of jpeg file", for the picture can be opened successful but computer cannot recognize
owner: Tu Jiahan
Date: 2020-08-30
"""

import os
import cv2

path = r'E:\work\SiamFC\siamfc-tensorflow\__Data\GOT-Curation\Data\VID\train\c\GOT-10k_Train_008761'
# path = r'E:\gitlab\tjh_tool\__Data'
directory = os.listdir(path)
for k in directory:
    dir_path = os.path.join(path, k)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            data = cv2.imread(file_path)
    print(k)