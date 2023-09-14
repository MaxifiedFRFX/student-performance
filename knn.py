# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:48:37 2023

@author: SERNi
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 

def knn(x_train, x_test, y_train, y_test):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train, y_train)      
    y_pred = knn.predict(x_test)
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred,))