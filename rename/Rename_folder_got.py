"""
Usage:Used for renaming file for got
owner:Tu Jiahan
Date:2020-09-08
"""
import os

PATH = 'E:\\dataset\\video_frame_json\\'

count = 0
for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        if dir.split('_')[-1] == 'xml':
            old = os.path.join(root, 'groundtruth.txt')
            new = os.path.join(root, 'Pic_json')
            os.rename(old, new)