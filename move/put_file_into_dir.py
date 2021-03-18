"""
Usage: used to make tracking file into their directory
owner: Tu Jiahan
Date: 2020-10-13
"""

import os
import shutil

INFRARED = False


if INFRARED:
    src_path = 'E:/dataset/tracking_frame/I20200923_raw'
    tar_path = 'E:/dataset/tracking_frame/I20200923'
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith('png'):
                filename = file.split('.')[0]
                jpg_file = filename + '.jpg'
                jpg_path = os.path.join(root, jpg_file)
                png_path = os.path.join(root, file)

                dir_name = filename[:13]
                save_dir = os.path.join(tar_path, dir_name)
                if not os.path.exists(save_dir):
                    os.mkdir(save_dir)

                shutil.copy(jpg_path, save_dir)
                shutil.copy(png_path, save_dir)

if not INFRARED:
    src_path = 'colorful'
    for root, dirs, files in os.walk(src_path):
        for file in files:
            filename = file.split('.')[0]
            file_path = os.path.join(root, file)
            dir_name = filename[:13]
            save_dir = os.path.join(root, dir_name)
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            shutil.move(file_path, save_dir)