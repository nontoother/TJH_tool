"""
Usage: Used for transferring frames to video. For Gongansansuo.
owner: Tu Jiahan
Date: 2020-09-17
"""

import os
import cv2

frame_get_path = './__Data/corridor/1/'
video_save_path = './__Data/corridor/1/1.mp4'

# 视频每秒25帧
fps = 25
# 需要转为视频的图片的尺寸
size = (1920, 1080)
# 可以使用cv2.resize()进行修改


def frame2video(fps, save_path, frames_path):
    video = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    filelist = os.listdir(frames_path)
    filelist.sort(key=lambda x: int(x.replace("video_1_", "").split('.')[0]))
    # filelist.sort(key=lambda x: int(x.split('.')[0]))
    for item in filelist:
        if item.endswith('.jpg'):
            # 找到路径中所有后缀名为.jpg的文件，可以更换为.jpg或其它
            item_path = os.path.join(frames_path, item)
            img = cv2.imread(item_path)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    frame2video(25, video_save_path, frame_get_path)
