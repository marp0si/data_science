# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:30:44 2022

@author: _s1n4n_
"""
import numpy as np

'''def naive_relu(x):
    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=max(x[i,j],0)
            x_relu=x[i,j]
    return x
'''
'''
def naive_relu(x,y):
    assert x.shape==(4,),f"got: {(x.shape)}"
    assert x.shape==y.shape
    x=x.copy()
    for i in list(x[0].shape):
        for j in list(x[1].shape):
            x[i,j]+=y[i,j]
    return x,y
'''
x=np.array([1, 2, 3, 4])
y=np.array([5, 6, 7, 8])
#print(naive_relu(x[0],x[1]))
#z=np.maximum(x+y,0)# eleman bazlı relu=> [6,8,10,12]
