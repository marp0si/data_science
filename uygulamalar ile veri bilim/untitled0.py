# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 14:53:23 2023

@author: PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
baslık=['kullanıcıid','filmid','değerlendirme',"zaman dalgası"]
df=pd.read_csv('ml-100k/u.data',sep='\t',names=baslık)
kullanıcı_say=df.kullanıcıid.unique().shape[0]
film_say=df.filmid.unique().shape[0]

print(kullanıcı_say)
'''
print(f'kullanıcı sayısı= {kullanıcı_say},film say= {film_say}')
print(df.head())

plot.rc('font',size=10)
df.değerlendirme.value_counts(sort=False).plot(kind='bar')
plot.title("değerlendirme dağılımı")
plot.xlabel("değer")
plot.ylabel("beğeni sayısı")
plot.show()
'''
df_ort=pd.DataFrame(round(df.groupby('filmid')['değerlendirme'].mean(),2))
df_ort['DsTemp']=pd.DataFrame(df.groupby('filmid')['değerlendirme'].count())
df_ort.columns=['değerOrtalamas','değerSayısı']
'''
print(df_ort.sort_values('değerSayısı',ascending=False).head())
'''
kuMatris=np.zeros((kullanıcı_say,film_say))
for line in df.itertuples():
    kuMatris[line[1]-1,line[2]-1]=line[3]
'''print(kuMatris.shape)   (943, 1682) '''

from sklearn.metrics.pairwise import pairwise_distances
kullanıcı_benzerlik=pairwise_distances(kuMatris,metric='cosine')
'''print(kullanıcı_benzerlik.shape) (943, 943)'''
def tahmin(değerlendirme ,kullanıcı_benzerlik):
    ortalama_değerlendirme=değerlendirme.mean(axis=1)
    değerlendirme_farkı=(değerlendirme-ortalama_değerlendirme[:,np.newaxis])
    tahmin=ortalama_değerlendirme[:,np.newaxis]+kullanıcı_benzerlik.dot(değerlendirme_farkı)/np.array([np.abs(kullanıcı_benzerlik).sum(axis=1)]).T
    return tahmin
kullanıcı_tahmin=tahmin(kuMatris,kullanıcı_benzerlik)
'''print(kullanıcı_tahmin)'''

#kullanıcı ürün değerlendirmesinin seyrekliği
seyreklik=round(1.0-len(df)/float(kullanıcı_say*film_say),4)*100
#print(f'syreklik= %{seyreklik}')

#SVD hesaplama (X=U*S*V**T)
import scipy.sparse as sp
from scipy.sparse.linalg import svds
U,S,vt=svds(kuMatris,k=30)
#print(U.shape) (943, 30)

# tavsiye sistemlerinin değerlendirme ölçütü 
from sklearn.metrics import mean_squared_error
from math import sqrt
def rmse_hesapla(tahmin,referans_Veri):
    tahmin=tahmin[referans_Veri.nonzero()].fatten()
    referans_Veri=referans_Veri[referans_Veri.nonzero()].fatten()
    return sqrt(mean_squared_error(tahmin, referans_Veri))
# rmse değerlendirme ölçütünün hesaplanması
from sklearn import model_selection as ms
train,test=ms.train_test_split(df,test_size=0.30)

kuMatrix_train=np.zeros((kullanıcı_say,film_say))
for line in train.itertuples():
    kuMatrix_train[line[1]-1,line[2]-1]=line[3]

kuMatrix_test=np.zeros((kullanıcı_say,film_say))
for line in test.itertuples():
    kuMatrix_test[line[1]-1,line[2]-1]=line[3]
#kullanıcılar arası benzerlik hesaplama
from sklearn.metrics.pairwise import pairwise_distances
kullanıcı_benzerlik=pairwise_distances(kuMatrix_train,metric='cosine')
kullanıcı_tahmin=tahmin(kuMatrix_train,kullanıcı_benzerlik)
print(kullanıcı_tahmin)
