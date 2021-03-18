import os

path = r'E:\work\SiamFC\siamfc-tensorflow\__Data\GOT-Curation\Data\VID\train'
# path = r'E:\gitlab\patch-2\Project\TJH_doc'
count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if file.split('.')[-1] == 'jpg':
            count += 1
            if count%10000 == 0:
                print(count)
print(count)