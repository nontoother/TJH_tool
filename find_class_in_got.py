import cv2
import os
import configparser

path = 'E:/dataset/GOT/train'

count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('ini'):
            conf = configparser.ConfigParser()
            src_path = os.path.join(root, file)
            conf.read(src_path)
            # if conf.get("METAINFO", "root_class") == 'animal':
            if conf.get("METAINFO", "major_class") == 'canine':     # 找狗的类别
                print(root)
                count += 1
                # if count % 500 == 0:
print(count)