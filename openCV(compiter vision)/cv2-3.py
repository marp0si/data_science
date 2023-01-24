# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:01:46 2023

@author: sino
"""
import cv2
import numpy as np
import time

image_path = "dsadas.jpg"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 1), int(image.shape[1] * 1)))
image_shape = image.shape
'''puting text
text = "This is a girl image"
position = (30, 50)  # Left-Bottom
color = (0, 0, 255)  # Blue Green Red
font_size = 1
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text, position, font, font_size, color, thickness)

'''
''' circle 
center_point = (int(image_shape[0] * 0.5), int(image_shape[1] * 0.5))
radius = 100
cv2.circle(image, center_point, radius, (0, 255, 0), thickness=2)

cv2.imshow("Reading Image", image)
'''

'''
LİNE
point1 = (int(image_shape[0] * 0.1), int(image_shape[1] * 0.1))
point2 = (int(image_shape[0] * 0.9), int(image_shape[1] * 0.9))
cv2.line(image, point1, point2, (0, 255, 0), thickness=2)
'''
'''image = cv2.arrowedLine(image, (int(image.shape[0] * 0.1), int(image.shape[1] * 0.1)),
                        (int(image.shape[0] * 0.9), int(image.shape[1] * 0.9)),
                        (0, 0, 255), 5)
'''
'''
rectangle
point1 = (int(image_shape[0] * 0.1), int(image_shape[1] * 0.1))
point2 = (int(image_shape[0] * 0.9), int(image_shape[1] * 0.9))
cv2.rectangle(image, point1, point2, (0, 255, 0), thickness=2)
'''

''' polygons 
pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)

image = cv2.polylines(image, [pts],
                      isClosed=True, color=(0, 0, 255), thickness=5)
''' 
'''clipline
colors={'red':(0,0,255),'blue':(255,0,0),'yellow':(0,255,255)}
#cv2.line(image, (0, 0), (300, 300), colors['red'], 3)
#cv2.rectangle(image, (0, 0), (100, 100), colors['blue'], 3)
ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300))
if ret:
    cv2.line(image, p1, p2, colors['yellow'], 3)
'''


'''
animated rainbow
x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6 = 25, 25, 110, 200, 200, 110, 70, 160, 200, 160, 70, 20
#color = random.choice(colors)
for i in range(100):
    x1 += 4
    x2 += 4
    x3 += 4
    x4 += 4
    x5 += 4
    x6 += 4

    y1 += 4
    y2 += 4
    y3 += 4
    y4 -= 4
    y5 -= 4
    y6 -= 4

    pts = np.array([[x1, y1], [x2, y2],
                    [x3, y3], [x4, y4],
                    [x5, y5], [x6, y6]],
                   np.int32)

    image = cv2.polylines(image, [pts],
                          isClosed=True, color=(0, 0, 255), thickness=2)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

    cv2.imshow("Reading Image", image)

    cv2.waitKey(50)
'''
cv2.imshow("Reading Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

