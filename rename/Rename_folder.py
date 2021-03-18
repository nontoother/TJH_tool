"""
Usage:Used for renaming folder
owner:Tu Jiahan
Date:2020-09-08
"""
import os

PATH = 'E:/dataset/tracking_labelled/infrared'

count = 0
for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        if len(dir) > 9:
            dir_new = dir[:13]
            old = os.path.join(root, dir)
            new = os.path.join(root, dir_new)
            os.rename(old, new)
        # if dir.split('_')[-1] == 'xml':
        #     old = os.path.join(root, dir)
        #     new = os.path.join(root, 'Pic_json')
        #     os.rename(old, new)