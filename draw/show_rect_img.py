"""
Usage: Draw a specific rectangle on the colorful image to see the infrared range.
owner: Tu Jiahan
Date: 2020-09-28
"""
import cv2


def get_rect(cxmin, cymin, cxmax, cymax, ixmin, iymin, ixmax, iymax):
    cwidth = cxmax - cxmin
    iwidth = ixmax - ixmin
    cheight = cymax - cymin
    iheight = iymax - iymin
    width_ratio = cwidth / iwidth
    height_ratio = cheight / iheight
    ctop = iymin * height_ratio
    cleft = ixmin * width_ratio
    cbutton = (1024 - iymax) * height_ratio
    cright = (1280 - ixmax) * width_ratio
    rect_xmin = int(cxmin - cleft)
    rect_ymin = int(cymin - ctop)
    rect_xmax = int(cxmax + cright)
    rect_ymax = int(cymax + cbutton)

    return rect_xmin, rect_ymin, rect_xmax, rect_ymax


rect_xmin, rect_ymin, rect_xmax, rect_ymax = get_rect(951, 151, 1107, 523, 535, 129, 802, 756)
print(rect_xmin, rect_ymin, rect_xmax, rect_ymax)
image = cv2.imread("E:/gitlab/video_filter/src_img.jpg")
rect_img = cv2.rectangle(image, (rect_xmin, rect_ymin), (rect_xmax, rect_ymax), (0, 0, 255))
cv2.imshow('img', rect_img)
cv2.waitKey(0)
cv2.imwrite("C:/Users/TJH/Desktop/label/rect_img.jpg", rect_img)