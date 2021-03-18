"""
Usage: Used for making an easy tracking frame to see the difference between cross-correlation and convolution
owner: Tu Jiahan
Date: 2020-11-24
"""
import numpy as np
import os
import time
from PIL import Image, ImageDraw
import cv2
import tensorflow as tf


DATA_PATH = '../__Result/test'


def generate():
    img = Image.new("RGB", (1920, 1080), (255, 255, 255))
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('white', img)
    # cv2.waitKey(0)
    cv2.imwrite('../canvas.jpg', img)
    times = 100
    x = 500
    y = 250
    r = 100
    for k in range(times):
        img = Image.open("../canvas.jpg")
        draw = ImageDraw.Draw(img)
        k1 = 5*k
        draw.ellipse((x+k1 - r, y+k1 - r, x+k1 + r, y+k1 + r), fill=(255, 0, 0))
        frame_name = '%05d' % (k+1) + '.jpg'
        img.save('./__Result/test/{}'.format(frame_name))
# frame_name = name.split('.')[0] + '%05d' % count + '.jpg'

def create_video_writer(data_save_dir):
    current_time_stamp = time.gmtime()
    year = current_time_stamp.tm_year
    month = current_time_stamp.tm_mon
    date = current_time_stamp.tm_mday
    hour = current_time_stamp.tm_hour
    minutes = current_time_stamp.tm_min
    seconds = current_time_stamp.tm_sec

    file_name = "%04d%02d%02d%02d%02d%02d.mp4" % (year, month, date, hour, minutes, seconds)
    file_path = os.path.join(data_save_dir, file_name)
    writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, (1920, 1080))       # 需要根据图片的尺寸进行修改，且main函数里面的也要改

    return writer


def shutdown_writer(writer):
    writer.release()
    writer = None


def make_video():
    writer = create_video_writer(DATA_PATH)
    for i in range(100):
        file_path = os.path.join(DATA_PATH, "{}.jpg".format(i+1))
        frame = cv2.imread(file_path)
        writer.write(frame)

    shutdown_writer(writer)


def main():
    generate()
    # make_video()


if __name__ == '__main__':
    main()