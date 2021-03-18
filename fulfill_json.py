"""
Usage:Used for making annotation file(xml) into json
owner:Tu Jiahan
Date:2020-06-19
"""
import os
import json

path = r'E:\dataset\video_frame_json\35'

for root, dirs, files in os.walk(path):
    for file in files:
        file_name = file.split('.')
        if file_name[-1] == 'jpg':
            json_name = file_name[0] + '.json'
            json_path = os.path.join(path, 'Pic_json', json_name)
            k = path.split('\\')[-1]
            if not os.path.exists(json_path):
                jsontext = {
                    "annotation": {
                        "folder": "1",
                        "filename": "video_{}_{}.jpg".format(k, file_name[0]),
                        "path": "/home/gc/gosun/test/20200615_bj/{}/video_{}_{}.jpg".format(k, k, file_name[0]),
                        "source": {
                            'database': 'unknown'
                        },
                        "size": {
                            'width': '1920',
                            'height': '1080',
                            'depth': '3'
                        },
                        "segmented": "0"}

                }
                jsondata = json.dumps(jsontext, indent=2, separators=(',', ':'))
                f = open(json_path, 'w+')
                f.write(jsondata)
                f.close()