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
import knn
import dt
import lr
import svm
import ann
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

pd.set_option('display.max_columns', 8)

math = pd.read_csv('student/student-mat.csv', delimiter=';')
portuguese = pd.read_csv('student/student-por.csv', delimiter=';')

cleaner.clean_student_performance(math)
cleaner.clean_student_performance(portuguese)

le = preprocessing.LabelEncoder()
for column_name, column_data in math.items():
    if column_data.dtype != "int64":
        math[column_name] = le.fit_transform(list(math[column_name]))
for column_name, column_data in portuguese.items():
    if column_data.dtype != "int64":
        portuguese[column_name] = le.fit_transform(list(portuguese[column_name]))

labels = ["F - Poor", "C - Sufficient", "B/A - Good"]
bins = [-1, 9, 13, 20]
math['bins'] = pd.cut(math['G3'], bins=bins, labels=labels)
portuguese['bins'] = pd.cut(portuguese['G3'], bins=bins, labels=labels)

print("=======================Count how many are in math grade range=======================")
print(math['bins'].value_counts())
print("=======================Count how many are in Portugueses grade range=======================")
print(portuguese['bins'].value_counts())

print("=======================Head of Math Data Set=======================")
print(math.head())
print("=======================Head of Portuguese Data Set=======================")
print(portuguese.head())

math_x = math.iloc[:, :-3].values
math_y = math.iloc[:, -1].values
port_x = portuguese.iloc[:, :-3].values
port_y = portuguese.iloc[:, -1].values

math_x_train,math_x_test,math_y_train,math_y_test = train_test_split(math_x,math_y,test_size=0.28,random_state=42,stratify=math_y)
port_x_train,port_x_test,port_y_train,port_y_test = train_test_split(port_x,port_y,test_size=0.28,random_state=42,stratify=port_y)

print("=======================Count how many are in port y test grade range=======================")
print(port_y_test.value_counts())
print("=======================Count how many are in port y train  grade range=======================")
print(port_y_train.value_counts())

print("=======================KNN Results=======================")
print("------Math Class Dataset------")
knn.knn(math_x_train, math_x_test, math_y_train, math_y_test)
print("------Portuguese Class Dataset------")
knn.knn(port_x_train, port_x_test, port_y_train, port_y_test)

print("=======================Decision Tree Results=======================")
print("------Math Class Dataset------")
dt.dt(math_x_train, math_x_test, math_y_train, math_y_test)
print("------Portuguese Class Dataset------")
dt.dt(port_x_train, port_x_test, port_y_train, port_y_test)

print("=======================Logistic Regression=======================")
print("------Math Class Dataset------")
lr.lr(math_x_train, math_x_test, math_y_train, math_y_test)
print("------Portuguese Class Dataset------")
lr.lr(port_x_train, port_x_test, port_y_train, port_y_test)

print("=======================Support Vector Machines=======================")
print("------Math Class Dataset------")
svm.svm(math_x_train, math_x_test, math_y_train, math_y_test)
print("------Portuguese Class Dataset------")
svm.svm(port_x_train, port_x_test, port_y_train, port_y_test)

print("=======================Multi-layer Preceptron=======================")
print("------Math Class Dataset------")
ann.ann(math_x_train, math_x_test, math_y_train, math_y_test)
print("------Portuguese Class Dataset------")
ann.ann(port_x_train, port_x_test, port_y_train, port_y_test)
