"""
Usage: Used for making the .avi readable
owner: Tu Jiahan
Date: 2020-09-17
"""

import os
import cv2
import time

start_frame = 1
stop_frame = 82500

VIDEO_FILE = r"E:/Infraredfile/洪园224_赣青云谱洪园7栋东侧充电桩热成像_20200615060300_20200615065912.avi"
DATA_SAVE_DIR = r"E:/Infraredfile/7"

writer = None


def create_video_writer():
    global writer
    current_time_stamp = time.gmtime()
    year = current_time_stamp.tm_year
    month = current_time_stamp.tm_mon
    date = current_time_stamp.tm_mday
    hour = current_time_stamp.tm_hour
    minutes = current_time_stamp.tm_min
    seconds = current_time_stamp.tm_sec

    file_name = "%04d%02d%02d%02d%02d%02d.mp4" % (year, month, date, hour, minutes, seconds)
    file_path = os.path.join(DATA_SAVE_DIR, file_name)
    writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, (1280, 960))


def shutdown_writer():
    global writer
    writer.release()
    writer = None


def main():
    global writer
    writer = None

    if os.path.exists(VIDEO_FILE) is False:
        raise ValueError("video directory does not exist, quit")

    if os.path.exists(DATA_SAVE_DIR) is False:
        os.mkdir(DATA_SAVE_DIR)

    cap = cv2.VideoCapture(VIDEO_FILE)

    video_count = 0

    while True:
        ret, frame = cap.read()

        if ret is False:
            continue
        else:
            output_frame = frame
            video_count += 1

            if video_count == start_frame:
                create_video_writer()
                writer.write(output_frame)
            elif start_frame < video_count < stop_frame:
                writer.write(output_frame)
            elif video_count == stop_frame:
                shutdown_writer()

            if video_count % 1000 == 0:
                print(video_count)


if __name__ == "__main__":
    main()