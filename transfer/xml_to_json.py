"""
Usage:Used for making annotation file(xml) into json
owner:Tu Jiahan
Date:2020-06-19
"""
import xmltodict
import json
import os

PATH = r'E:\dataset\video_frame_json\35\Pic_json'

count = 0
for root, dirs, files in os.walk(PATH):
    for file in files:
        if file.split('.')[-1] == 'mp4' or file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'json':
            continue
        xml_path = os.path.join(root, file)
        xml_file = open(xml_path, 'r', encoding="utf-8")
        xml_str = xml_file.read()
        json_dict = xmltodict.parse(xml_str)
        # json_str = json.dumps(json_dict, indent=2)
        with open(xml_path, "w+", encoding="utf-8") as f:
            json.dump(json_dict, f, indent=2, ensure_ascii=False)  # ensure_ascii确保中文不会乱码
        xml_file.close()
        name = file.split('.')[0]
        new_name = name + '.json'
        new_path = os.path.join(root, new_name)
        os.rename(xml_path, new_path)
        count += 1
        if count % 1000 == 0:
            print("num:", count)