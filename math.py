# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:30:44 2022

@author: _s1n4n_
np.maximum(x+y,0)#
np.dot(x,y)
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

x=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
#2 boyut ve 1 boyutlu diziler ile 
'''
def naive_add_matrix_and_vector(x,y):
    assert len(x.shape)==2,f'{x.shape}'
    assert len(y.shape)==1,f'{y.shape}'
    assert x.shape[1]==y.shape[0]
    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]+=y[j]
    return x
print(naive_add_matrix_and_vector(x,y)) #[[ 6  8 10 12][10 12 14 16]]
'''
z=np.maximum(x+y,0)#[6 8 10 12][10 12 14 16]


x=np.array([1, 2, 3, 4])
y=np.array([5, 6, 7, 8])

'''
def naive_vector_dot(x,y):
    assert len(x.shape)==1,f'{x.shape}'
    assert len(y.shape)==1,f'{y.shape}'
    assert x.shape[0]==y.shape[0]
    z=0
    for i in range(x.shape[0]):
            z+=x[i]*y[i]
    return z
x=np.array([1, 2, 3, 4])
y=np.array([5, 6, 7, 8])
print(naive_vector_dot(x,y)) #70'''
z=np.dot(x,y)#70
'''
matris ve vektör
x=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
y=np.array([5, 6, 7, 8])
def naive_dot_matrix_and_vector(x,y):
    assert len(x.shape)==2,f'{x.shape}'
    assert len(y.shape)==1,f'{y.shape}'
    assert x.shape[1]==y.shape[0]
    x=x.copy()
    z=np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i]+=x[i,j]*y[j]
    return z
print(naive_dot_matrix_and_vector(x,y)) #[70 174]
'''
#matrix çarpımı
'''
x = np.random.random((5,2))
y = np.random.random((2,5))
def naive_vector_dot(x,y):
    assert len(x.shape)==1,f'{x.shape}'
    assert len(y.shape)==1,f'{y.shape}'
    assert x.shape[0]==y.shape[0]
    z=0
    for i in range(x.shape[0]):
            z+=x[i]*y[i]
    return z
def naive_dot_matrixs(x,y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]
    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)
    return z
print(naive_dot_matrixs(x,y)) #[70 174]
'''


