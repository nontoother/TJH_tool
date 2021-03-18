"""
Usage: Used for transferring video to frames. One can change name or save structure depend on needs.
owner: Tu Jiahan
Date: 2020-07-20
"""

import os
import cv2

all_videos_path = './__Data/infrared'


def video2frame(video_path, save_dir):

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        count += 1
        if count >= 5500:
            print('start')
            cv2.imshow('img', image)
            cv2.waitKey(1)
            cv2.imwrite(os.path.join(save_dir, '{}.jpg'.format(count)), image)
    print(count)


if __name__ == '__main__':
    all_videos = os.listdir(all_videos_path)
    for video in all_videos:
        video_path = os.path.join(all_videos_path, video)
        video_name = video.split('.')[0]
        if video_name == 'co':
            save_dir = os.path.join(all_videos_path, video_name)
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            video2frame(video_path, save_dir)

