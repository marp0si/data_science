# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:33:49 2023

@author: PC
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
baslık=['kullanıcıid','filmid','değerlendirme',"zaman dalgası"]
df=pd.read_csv('ml-100k/u.data',sep='\t',names=baslık)
kullanıcı_say=df.kullanıcıid.unique().shape[0]
film_say=df.filmid.unique().shape[0]
kuMatris=np.zeros((kullanıcı_say,film_say))
for line in df.itertuples():
    print(len(kuMatris))
    
