"""
Usage: Used for transferring frames to video. More stable version.
owner: Tu Jiahan
Date: 2020-09-17
"""


import cv2
import os
import time


DATA_PATH = 'E:/work/SiamFC/siamfc-tensorflow/Logs/SiamFC/track_model_inference/SiamFC-3s-color-scratch/202008280001/test'
# DATA_SAVE_DIR = '__Data/tracking_demo'


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


def txt_reader(txt_path, dir_name, data_save_dir):
    count = 0
    writer = create_video_writer(data_save_dir)

    with open(txt_path, "r") as f:
        for line in f.readlines():
            count += 1
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            line = line.split(',')
            xmin = int(float(line[0]))
            ymin = int(float(line[1]))
            width = int(float(line[2]))
            height = int(float(line[3]))
            xmax = xmin + width
            ymax = ymin + height
            file_path = os.path.join('E:/work/SiamFC/siamfc-tensorflow/new', dir_name, "{}{:05d}.jpg".format(dir_name, count))
            try:
                frame = cv2.imread(file_path)
                frame = cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), thickness=2)
                # cv2.imshow('img', frame)
                # cv2.waitKey(0)
                writer.write(frame)
            except:
                break

    shutdown_writer(writer)


if __name__ == '__main__':
    # 需要画框的转换
    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            if file.endswith('txt'):
                txt_path = os.path.join(root, file)
                dir_name = root.split('\\')[-1]
                txt_reader(txt_path, dir_name, root)
    # 不需要画框的转换
    # writer = create_video_writer(DATA_PATH)
    # for root, dirs, files in os.walk(DATA_PATH):
    #     for file in files:
    #         if file.endswith('jpg'):
    #             frame = cv2.imread(os.path.join(root, file))
    #             cv2.imshow('img', frame)
    #             cv2.waitKey(1)
    #             writer.write(frame)
    # shutdown_writer(writer)