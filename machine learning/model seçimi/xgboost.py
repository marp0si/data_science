import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('Churn_Modelling.csv')

X= veriler.iloc[:1000,3:13].values
Y = veriler.iloc[:1000,13].values
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
labelencoder_X_1=LabelEncoder()
X[:,1]=labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2=LabelEncoder()
X[:,2]=labelencoder_X_1.fit_transform(X[:,2])
ohe=OneHotEncoder()
X=ohe.fit_transform(X).toarray()
X=X[:,1:]
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

from xgboost import XGBClassifier 
classifier=XGBClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_train)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_pred,y_test)
print(cm)