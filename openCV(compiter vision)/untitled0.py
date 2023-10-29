# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:47:53 2023

@author: PC
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(5,4)
plt.rcParams['İmage.İnterpolation']='nearest'
plt.rcParams['image.cmap']='gray'
np.random.seed(1)

def zero_pad(x,pad):
    x_pad=np.pad(x,((0,0),(pad,pad),(pad,pad),(0,0)),'constant',constant_values)
    return x_pad
np.random.seed(1)
x=np.random.randn(4,3,3,2)
print('x_shape=',x.shape)
print('x_pad.shape:',x_pad.shape)
print('x[1,1]:',x[1,1])
print('x_pad[1,1]:',x_pad[1,1])
fig.axarr=plt.subplots(1,2)
axarr[0].set_title('x')
axarr[0].imshow(x[0,:,:0])
axarr[0].set_title('x_pad')
axarr[0].imshow(x_pad[0,:,:0])
