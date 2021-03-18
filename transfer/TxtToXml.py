"""
Usage: Used for adapting to ImageNet data structure to test SiamFC, make GOT annotations(TXT) into xml format
owner: Tu Jiahan
Date: 2020-07-15
"""

import os
from xml.dom.minidom import Document
from collections import defaultdict
import cv2 as cv


class OpeateXML:

    def __init__(self, srcPath: str, targetPath: str, srcFileName: str):
        self._srcPath = srcPath
        self._targetPath = targetPath
        self._srcFileName = srcFileName

    def readSrcFileName(self, fileEncoding="utf8") -> dict:
        data = defaultdict(list)
        # s = re.compile("\.AIpng_\d{1,}", re.IGNORECASE)
        srcFileFullPath = os.path.join(self._srcPath, self._srcFileName)
        try:
            # with open(srcFileFullPath, mode="r", encoding=fileEncoding, errors="ignore") as fr:
            with open(srcFileFullPath, 'r') as fr:
                for content in fr.readlines():
                    # data[s.sub(".AIpng", content.strip().split(",")[0])].append(content.strip())
                    data['a'].append(content.strip())
        except Exception as ex:
            # MyLogger().error(f"OperateXML:read file error:\n{ex}")
            print("OperateXML:read file error")
            return {}
        else:
            # data.sort(key=lambda x: x.strip().split(",")[0])
            return data

    def createXML(self, data: dict, srcPath: str, targetPath: str, fileEncoding="utf-8"):
        if data:
            try:
                count = 0
                for k, v in data.items():
                    for i in v:
                        count += 1
                        doc = Document()
                        # 创建根节点
                        rootNode = doc.createElement("annotation")
                        # 添加根节点
                        doc.appendChild(rootNode)

                        # 获得当前目录
                        curPath = targetPath.split('\\')[4:]
                        imgPath = os.path.join(srcPath, '00000001.jpg')
                        img = cv.imread(imgPath)
                        truewidth = img.shape[1]
                        trueheight = img.shape[0]

                        folder = doc.createElement("folder")
                        if curPath[-1].split('.')[-1] != 'xml':
                            nowPath = curPath[-2]+'/'+curPath[-1]   # for train data
                            # nowPath = curPath[-1]   # for val data

                        else:
                            nowPath = curPath[-3]+'/'+curPath[-2]   # for train data
                            # nowPath = curPath[-2]   # for val data
                        # folderText = doc.createTextNode("ILSVRC2015_VID_train_0000/ILSVRC2015_train_00000002")
                        # folderText = doc.createTextNode("ILSVRC2015_val_00000002")
                        folderText = doc.createTextNode(nowPath)
                        folder.appendChild(folderText)
                        rootNode.appendChild(folder)

                        filename = doc.createElement("filename")
                        no = str(count).zfill(8)
                        filenameText = doc.createTextNode(no)
                        filename.appendChild(filenameText)
                        rootNode.appendChild(filename)

                        source = doc.createElement("source")
                        rootNode.appendChild(source)
                        database = doc.createElement("database")
                        databaseText = doc.createTextNode('GOT')
                        database.appendChild(databaseText)
                        source.appendChild(database)

                        size = doc.createElement("size")
                        rootNode.appendChild(size)
                        width = doc.createElement("width")
                        widthText = doc.createTextNode(str(truewidth))
                        width.appendChild(widthText)
                        size.appendChild(width)
                        height = doc.createElement("height")
                        heightText = doc.createTextNode(str(trueheight))
                        height.appendChild(heightText)
                        size.appendChild(height)

                        tmpData = i.strip().split(",")

                        if len(tmpData) == 4:
                            # _, ymin, xmin, ymax, xmax, labelName = tmpData
                            left, top, width, height = tmpData
                            xmin = float(left) - 1
                            xmax = xmin + float(width) - 1
                            ymin = float(top) - 1
                            ymax = ymin + float(height) - 1
                            xmin = str(int(xmin))
                            xmax = str(int(xmax))
                            ymin = str(int(ymin))
                            ymax = str(int(ymax))
                            name = srcPath.split('\\')[-1].split('_')[-1]

                            objectObj = doc.createElement("object")
                            rootNode.appendChild(objectObj)

                            objecttrackid = doc.createElement("trackid")
                            objecttrackidText = doc.createTextNode('0')
                            objecttrackid.appendChild(objecttrackidText)
                            objectObj.appendChild(objecttrackid)

                            objectName = doc.createElement("name")
                            objectNameText = doc.createTextNode(name)
                            objectName.appendChild(objectNameText)
                            objectObj.appendChild(objectName)

                            objectBndBox = doc.createElement("bndbox")
                            objectObj.appendChild(objectBndBox)

                            objectBndBoxXmin = doc.createElement("xmin")
                            objectBndBoxYmin = doc.createElement("ymin")
                            objectBndBoxXmax = doc.createElement("xmax")
                            objectBndBoxYmax = doc.createElement("ymax")

                            objectBndBoxXminText = doc.createTextNode(xmin)
                            objectBndBoxYminText = doc.createTextNode(ymin)
                            objectBndBoxXmaxText = doc.createTextNode(xmax)
                            objectBndBoxYmaxText = doc.createTextNode(ymax)

                            objectBndBox.appendChild(objectBndBoxXmin)
                            objectBndBox.appendChild(objectBndBoxYmin)
                            objectBndBox.appendChild(objectBndBoxXmax)
                            objectBndBox.appendChild(objectBndBoxYmax)

                            objectBndBoxXmin.appendChild(objectBndBoxXminText)
                            objectBndBoxYmin.appendChild(objectBndBoxYminText)
                            objectBndBoxXmax.appendChild(objectBndBoxXmaxText)
                            objectBndBoxYmax.appendChild(objectBndBoxYmaxText)

                            objectObj.appendChild(objectBndBox)

                            objectoccluded = doc.createElement("occluded")
                            objectoccludedText = doc.createTextNode('1')
                            objectoccluded.appendChild(objectoccludedText)
                            objectObj.appendChild(objectoccluded)

                            objectgenerated = doc.createElement("generated")
                            objectgeneratedText = doc.createTextNode('0')
                            objectgenerated.appendChild(objectgeneratedText)
                            objectObj.appendChild(objectgenerated)
                        else:
                            continue

                        # save xml
                        # xmlName = os.path.splitext(k)[0] + ".xml"
                        xmlName = str(no) + ".xml"
                        targetPath = os.path.join(self._targetPath, xmlName)
                        with open(targetPath, mode="w", encoding=fileEncoding) as fw:
                            doc.writexml(fw, indent="\t", newl="\n", addindent="\t", encoding=fileEncoding)
            except Exception as ex:
                # MyLogger().error(f"OperateXML:Save xml error\n{ex}")
                print("OperateXML:Save file error")
                return


if __name__ == '__main__':
    path = r'E:\work\SiamFC\SiamFC-TensorFlow-got\data\TEST\Data\VID\train\GOT_train_0001'     # train path
    target = r'E:\work\SiamFC\SiamFC-TensorFlow-got\data\TEST\Annotations\VID\train\GOT_train_0001'    # train path
    srcName = "groundtruth.txt"
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            count = dir.split('_')[-1]
            if len(count) == 6:
                # and int(count) > 2500:
                srcPath = os.path.join(root, dir)
                targetPath = os.path.join(target, dir)
                if not os.path.exists(targetPath):
                    os.mkdir(targetPath)
                operateXML = OpeateXML(srcPath, targetPath, srcName)
                a = operateXML.readSrcFileName()
                operateXML.createXML(a, srcPath, targetPath)