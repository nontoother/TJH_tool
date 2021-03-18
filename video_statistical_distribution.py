"""
Usage: 用于得到每个视频的长度（帧数），并统计他们的分布
owner: Tu Jiahan
Date: 2020-10-10
"""

import os


path = 'E:/dataset/ILSVRC2015_part22/ILSVRC2015/Data/VID/val'
count = 0
pic_num = list()

for dir_name in os.listdir(path):
    count = 0
    dir_path = os.path.join(path, dir_name)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            count += 1
    if count != 0:
        pic_num.append(count)

print(pic_num)

array = [0 for _ in range(12)]
print(array)
for num in pic_num:
    num_series = int(num/100)
    # print(num_series)
    array[num_series] += 1

print(array)