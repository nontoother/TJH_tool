"""
Usage:Used for making annotation xml into what I need(in siamfc)
owner:Tu Jiahan
Date:2020-09-18
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


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


def write_xml(folder, videoname, filename, xmin, ymin, xmax, ymax, xml_path):
    dom = minidom.Document()
    # 文档根元素
    root = dom.createElement('annotation')
    dom.appendChild(root)

    # 文件夹路径
    NodeFolder = dom.createElement('folder')
    NodeFolder.appendChild(dom.createTextNode(folder))
    root.appendChild(NodeFolder)

    # 文件名
    NodeFilename = dom.createElement('filename')
    NodeFilename.appendChild(dom.createTextNode(filename))
    root.appendChild(NodeFilename)

    # 数据库
    NodeSource = dom.createElement('source')
    NodeDatabase = dom.createElement('database')
    NodeDatabase.appendChild(dom.createTextNode('TrackingDataset'))
    NodeSource.appendChild(NodeDatabase)
    root.appendChild(NodeSource)

    # 图片大小
    NodeSize = dom.createElement('size')
    NodeWidth = dom.createElement('width')
    NodeWidth.appendChild(dom.createTextNode('1920'))
    NodeSize.appendChild(NodeWidth)
    NodeHeight = dom.createElement('height')
    NodeHeight.appendChild(dom.createTextNode('1080'))
    NodeSize.appendChild(NodeHeight)
    root.appendChild(NodeSize)

    # 目标信息
    NodeObject = dom.createElement('object')
    NodeTrackid = dom.createElement('trackid')
    NodeTrackid.appendChild(dom.createTextNode('0'))
    NodeObject.appendChild(NodeTrackid)
    Nodename = dom.createElement('name')
    Nodename.appendChild(dom.createTextNode(videoname))
    NodeObject.appendChild(Nodename)

    # 目标信息中bndbox的坐标
    NodeBndbox = dom.createElement('bndbox')
    Nodexmin = dom.createElement('xmin')
    Nodexmin.appendChild(dom.createTextNode(xmin))
    NodeBndbox.appendChild(Nodexmin)
    Nodeymin = dom.createElement('ymin')
    Nodeymin.appendChild(dom.createTextNode(ymin))
    NodeBndbox.appendChild(Nodeymin)
    Nodexmax = dom.createElement('xmax')
    Nodexmax.appendChild(dom.createTextNode(xmax))
    NodeBndbox.appendChild(Nodexmax)
    Nodeymax = dom.createElement('ymax')
    Nodeymax.appendChild(dom.createTextNode(ymax))
    NodeBndbox.appendChild(Nodeymax)
    NodeObject.appendChild(NodeBndbox)

    # 目标信息中剩下的信息
    NodeOccluded = dom.createElement('occluded')
    NodeOccluded.appendChild(dom.createTextNode('1'))
    NodeObject.appendChild(NodeOccluded)
    NodeGenerated = dom.createElement('generated')
    NodeGenerated.appendChild(dom.createTextNode('0'))
    NodeObject.appendChild(NodeGenerated)

    root.appendChild(NodeObject)

    fp = open(xml_path, 'w')
    dom.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


path = 'E:/work/SiamFC/siamfc-tensorflow/__Data/tracking/Annotations/VID/train/tracking_train_0000/202009040003'
# path = '20200828001300001.xml'
for root, dirs, files in os.walk(path):
    for file in files:
        src_path = os.path.join(root, file)
        videoname, filename, xmin, ymin, xmax, ymax = read_xml(src_path)
        folder_name = root.split('/')[-1]
        folder = 'tracking_train_0000/' + folder_name
        write_xml(folder, videoname, filename, xmin, ymin, xmax, ymax, src_path)
