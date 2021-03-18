"""
Usage: Used for synchronizing infrared video and colorful video
owner: Tu Jiahan
Date: 2020-10-17
"""

import os
import cv2
import time
import numpy as np


def create_video_writer(DATA_SAVE_DIR, width, height):
    """
    used to create video writer
    :param DATA_SAVE_DIR: video save place
    :param width: video's width
    :param height: video's height
    :return: writer
    """
    current_time_stamp = time.gmtime()
    year = current_time_stamp.tm_year
    month = current_time_stamp.tm_mon
    date = current_time_stamp.tm_mday
    hour = current_time_stamp.tm_hour
    minutes = current_time_stamp.tm_min
    seconds = current_time_stamp.tm_sec

    file_name = "%04d%02d%02d%02d%02d%02d.mp4" % (year, month, date, hour, minutes, seconds)
    file_path = os.path.join(DATA_SAVE_DIR, file_name)
    videowriter = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, (width, height))

    return videowriter


def shutdown_writer(writer):
    """
    used to close video writer
    :return: None
    """
    writer.release()
    writer = None


def main():

    path = ''
    data_save_dir = ''
    cap = cv2.VideoCapture(path)

    if os.path.exists(data_save_dir) is False:
        os.mkdir(data_save_dir)

    frame_num_path = ''
    frame_num_list = np.load(frame_num_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    video_num = 0  # 记录是第几个视频，即frame_num_list的脚标
    count = 0
    success = cap.isOpened()

    while success:

        success, frame = cap.read()
        if count == frame_num_list[video_num][0]:
            writer = create_video_writer(data_save_dir, width, height)
            writer.write(frame)
            video_num += 1

        elif frame_num_list[video_num][0] < count < frame_num_list[video_num][1]:
            writer.write(frame)

        if count == frame_num_list[video_num][1]:
            shutdown_writer(writer)
            break

        count += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
