"""
Usage: Used for transferring float data in .txt into int, and cover the old float data
owner: Tu Jiahan
Date: 2020-07-20
"""

from collections import defaultdict
import os

path = r'E:\work\SiamFC\SiamFC-TensorFlow-got\test'
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.txt'):
            new_path = os.path.join(root, file)
            lines = open(new_path, 'r').readlines()
            data = defaultdict(list)
            with open(new_path, 'r') as fr:
                for content in fr.readlines():
                    data['a'].append(content.strip())
            with open(new_path, 'w') as fw:
                for k, v in data.items():
                    for i in v:
                        tmpData = i.strip().split(",")
                        if len(tmpData) == 4:
                            a, b, c, d = tmpData
                            a = int(float(a))
                            b = int(float(b))
                            c = int(float(c))
                            d = int(float(d))
                            fw.write('{},{},{},{}'.format(a, b, c, d) + "\n")

