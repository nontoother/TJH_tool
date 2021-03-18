"""
Usage: Used for cutting out the required box on the video and resize to ideal size
owner: Tu Jiahan
Date: 2020-09-08
"""

import cv2
import os
src_path = r'E:\gitlab\tjh_tool\__Data\corridor\1.mp4'
save_path = r'E:\gitlab\tjh_tool\__Data\corridor'


def make_video():
    global writer
    vidcap = cv2.VideoCapture(src_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        crpped = image[311: 921, 652: 1413]
        final = cv2.resize(crpped, (1280, 1024))
        count += 1
        writer.write(final)


def create_video_writer():
    global writer
    file_name = "test.mp4"
    file_path = os.path.join(save_path, file_name)
    writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, (1280, 1024))       # 需要根据图片的尺寸进行修改，且main函数里面的也要改


def shutdown_writer():
    global writer
    writer.release()
    writer = None


if __name__ == '__main__':
    global writer
    writer = None
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)    # 设置为指定大小
    cv2.resizeWindow('Video', 1280, 1024)        # 设置为1280*720

    create_video_writer()
    make_video()
    shutdown_writer()
    cv2.destroyAllWindows()


