"""
Usage:Used for draw gt in the picture
owner:Tu Jiahan
Date:2020-09-18
"""

import xml.etree.ElementTree as ET
import os
import cv2

PATH = './__Data/202008280001'


def read_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text
    videoname = filename.split('.')[0][8:12]
    filename = filename.split('.')[0][12:]
    for Object in root.findall('object'):
        bndbox = Object.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text

        return videoname, filename, xmin, ymin, xmax, ymax


if __name__ == '__main__':
    for root, dirs, files in os.walk(PATH):
        for file in files:
            if file.endswith('jpg'):
                name = file.split('.')
                xml = name[0] + '.xml'
                file_path = os.path.join(root, file)
                xml_path = os.path.join(root, xml)
                videoname, filename, xmin, ymin, xmax, ymax = read_xml(xml_path)
                image = cv2.imread(file_path)
                cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 255, 255), thickness=2)
                cv2.imwrite(file_path, image)
                # cv2.imshow('img', image)
                # cv2.waitKey(0)