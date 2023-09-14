# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:28:40 2023

@author: SERNi
"""

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 

def ann(x_train, x_test, y_train, y_test):
    mlp = MLPClassifier(random_state=1, max_iter=10000).fit(x_train, y_train)
    print(mlp.score(x_test, y_test))

    y_pred = mlp.predict(x_test) 
    print("Confusion_matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred,))