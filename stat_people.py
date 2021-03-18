import os
import xml.etree.ElementTree as ET


path = 'E:/work/SiamFC/siamfc-tensorflow/__Data/tracking/Annotations/VID/train/tracking_train_0000'


def read_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for Object in root.findall('object'):
        bndbox = Object.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text

        return float(xmin), float(ymin), float(xmax), float(ymax)


count = 0
all_height = 0
all_width = 0
all_area = 0

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('xml'):
            xml_path = os.path.join(root, file)
            xmin, ymin, xmax, ymax = read_xml(xml_path)
            height = ymax - ymin
            width = xmax - xmin
            area = width * height
            if (3 * width) < height:
                all_height += height
                all_width += width
                all_area += area
                count += 1

mean_height = all_height/count
mean_width = all_width/count
mean_ratio = mean_height/mean_width
mean_area = all_area/count
print(mean_height)
print(mean_width)
print(mean_ratio)
print(mean_area)
