# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:36:46 2023

@author: SERNi
"""

from sklearn import tree
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 
from matplotlib import pyplot as plt

def dt(x_train, x_test, y_train, y_test):
    dt = tree.DecisionTreeClassifier()
    dt = dt.fit(x_train, y_train)   
    
    # Uncomment if you want to plot the data. It's a big picture,
    # so I didn't want to plot it every time.
    # fig = plt.figure(figsize=(120, 100))
    # _ = tree.plot_tree(dt, filled=True)
    
    y_pred = dt.predict(x_test)
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred,))