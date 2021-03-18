"""
Usage:Used for renaming file
owner:Tu Jiahan
Date:2020-09-08
"""

import os

PATH = 'E:/dataset/tracking_raw/infrared'

count = 0
for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        if dir == 'I20201021':
            date_path = os.path.join(root, dir)
            all_video = os.listdir(date_path)
            count = 0
            for video in all_video:
                count += 1
                video_name = dir + '%04d' % count + '.mp4'
                src_path = os.path.join(root, dir, video)
                new_path = os.path.join(root, dir, video_name)
                os.rename(src_path, new_path)

