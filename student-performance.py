# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:58:24 2023

@author: SERNi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:27:13 2023

@author: SERNi
"""

import pandas as pd
import cleaner
from sklearn.model_selection import train_test_split
from sklearn import tree
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

pd.set_option('display.max_columns', None)

math = pd.read_csv('student/student-mat.csv', delimiter=';')
portuguese = pd.read_csv('student/student-por.csv', delimiter=';')

# print(math.head())
# print(portuguese.head())

cleaner.clean_student_performance(math)
cleaner.clean_student_performance(portuguese)
for index, row in math.iloc[:, 31:33].iterrows():
    for prnt_educ in row:
        if prnt_educ not in range(0, 21):
            print(prnt_educ)

# print(math.iloc[:,3])



# =============================================================================
# X = data.drop(4,axis=1).values
# y = data[4].values
# print("Features:")
# print(X[:5])
# print("Labels:")
# print(y[:5])
# 
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=42,stratify=y)
# # =============================================================================
# # print("X_train")
# # print(X_train[:10])
# # print("y_train")
# # print(y_train[:10])
# # print("X_test")
# # print(X_test[:10])
# # print("y_test")
# # print(y_test[:10])
# # =============================================================================
# 
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X_train, y_train)
# 
# fig = plt.figure(figsize=(25,20))
# _ = tree.plot_tree(clf, filled=True)
# 
# dt_y_pred = clf.predict(X_test)
# print("Confusion_matrix for Decision Trees:")
# print(confusion_matrix(y_test, dt_y_pred))
# print("Classification Report for Decision Trees:")
# print(classification_report(y_test, dt_y_pred,))
# 
# logRegres = LogisticRegression(random_state=0, max_iter=1000).fit(X_train, y_train)
# print("Score for logistic regression")
# print(logRegres.score(X_test, y_test))
# 
# lr_y_pred = logRegres.predict(X_test)
# print("Confusion_matrix for logistic regression:")
# print(confusion_matrix(y_test, lr_y_pred))
# print("Classification Report for logistic regression:")
# print(classification_report(y_test, lr_y_pred,))
# 
# svc = SVC()
# svc.fit(X_train, y_train)
# svc_y_pred = svc.predict(X_test)
# print("Confusion_matrix for support vector machine:")
# print(confusion_matrix(y_test, svc_y_pred))
# print("Classification Report for support vector machine:")
# print(classification_report(y_test, svc_y_pred,))
# 
# mlp = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
# print(mlp.score(X_test, y_test))
# 
# mlp_y_pred = mlp.predict(X_test) 
# print("Confusion_matrix for MLP:")
# print(confusion_matrix(y_test, mlp_y_pred))
# print("Classification Report for MLP:")
# print(classification_report(y_test, mlp_y_pred,))
# =============================================================================
