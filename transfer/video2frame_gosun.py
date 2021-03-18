"""
Usage: Used for transferring video to frames. One can change name or save structure depend on needs.
owner: Tu Jiahan
Date: 2020-09-17
"""

import os
import cv2

data_path = 'E:/dataset/tracking_raw/train'
save_path = 'E:/dataset/tracking_frame'


def video2frame(video_path, name, save_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        count += 1
        frame_name = name.split('.')[0] + '%05d' % count + '.jpg'
        if success:
            # cv2.imwrite(os.path.join(save_path, '{}.jpg'.format(count)), image)
            cv2.imwrite(os.path.join(save_path, frame_name), image)
    print(count)


if __name__ == '__main__':
    for root, dirs, files in os.walk(data_path):
        for file in files:
            folder = root.split('\\')[-1]
            if folder == 'I20201021':
            # if (folder == '20200901') or (folder == '20200902') or (folder == '20200904'):
                frames_save_path = os.path.join(save_path, folder)
                if os.path.exists(frames_save_path) is False:
                    os.mkdir(frames_save_path)

                video_path = os.path.join(data_path, folder, file)
                video2frame(video_path, file, frames_save_path)

    # video_path = 'C:\\Users\\TJH\\Desktop\\abc\\20200923080100.mp4'
    # name = 'c'
    # save_path = 'C:\\Users\\TJH\\Desktop\\abc'
    # video2frame(video_path, name, save_path)
