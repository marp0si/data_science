# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 00:19:39 2022

@author: _S1n4n_
"""



import numpy as np
import pandas as pd
veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,3:].values

from sklearn.cluster import KMeans
kmeans = KMeans (n_clusters = 4, init='k-means++', random_state= 123)
Y_tahmin= kmeans.fit_predict(X)
asd=(X[Y_tahmin==0,0],X[Y_tahmin==0,1])
asd1=(X[Y_tahmin==1,0],X[Y_tahmin==1,1])
asd2=(X[Y_tahmin==2,0],X[Y_tahmin==2,1])
asd3=(X[Y_tahmin==3,0],X[Y_tahmin==3,1])


for i in asd1:
    print(i)