# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:10:17 2023

@author: SERNi
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 

def lr(x_train, x_test, y_train, y_test):
    logRegres = LogisticRegression(random_state=0, max_iter=10000).fit(x_train, y_train)
    print("Score for logistic regression")
    print(logRegres.score(x_test, y_test))
    
    y_pred = logRegres.predict(x_test)
    print("Confusion_matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))