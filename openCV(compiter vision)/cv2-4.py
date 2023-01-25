# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:39:18 2023

@author: sino
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
image = cv2.imread("../assets/globalaihub.png")
image = cv2.resize(image, (256, 128))

image_blur = cv2.blur(image, (5, 5))
image_gaussian = cv2.GaussianBlur(image, (5, 5), 0)
image_median = cv2.medianBlur(image, 5)
image_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

final_image = np.concatenate([image, image_blur, image_gaussian, image_median, image_bilateral], axis=0)

cv2.imshow("Final Image", final_image)
'''
#rotating 
'''
image_path = "dsadas.jpg"

image = cv2.imread(image_path)
image = cv2.resize(image, (256, 256))
image_shape = image.shape

image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image2 = cv2.rotate(image, cv2.ROTATE_180)
image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

vis = np.concatenate((image1, image2, image3), axis=1)

cv2.imshow("Reading All Images:", vis)
cv2.imshow("Reading Image 1", image1)
cv2.imshow("Reading Image 2", image2)
cv2.imshow("Reading Image 3", image3)

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, -angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result
cv2.imshow("Rotated Image", rotate_image(image, 60))
'''
'''
image_path = "paper_image.png"

image = cv2.imread(image_path)
image_shape = image.shape

pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (500, 600))

cv2.imshow('frame', image)
cv2.imshow('frame1', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#affine-transformations
'''
image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (256, 256))
image_shape = image.shape

rows, cols, ch = image.shape

pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(image, M, (cols, rows))

plt.subplot(121)
plt.imshow(image)
plt.title('Input')

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()
'''
#cropping-images
'''
image = cv2.imread("../assets/img.png")

x, y, w, h = 180, 65, 700, 750
cropped_image = image[y:y + h, x:x + w]

cv2.imshow("Cropped", cropped_image)
cv2.waitKey(0)
'''
cv2.destroyAllWindows()
cv2.waitKey(0)