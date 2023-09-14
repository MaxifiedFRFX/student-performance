# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:19:49 2023

@author: SERNi
"""

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 

def svm(x_train, x_test, y_train, y_test):
    svc = SVC()
    svc.fit(x_train, y_train)
    y_pred = svc.predict(x_test)
    print("Confusion_matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred,))