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
from sklearn.model_selection import train_test_split
from sklearn import linear_model, preprocessing

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

labels = ["F - Poor (Mau)", "F - Poor (Mediocre)", "C - Sufficient", "B - Good", "A - Very Good", "A+ - Excellent"]
bins = [-1, 6, 9, 13, 15, 17, 20]
math['bins'] = pd.cut(math['G3'], bins=bins, labels=labels)
portuguese['bins'] = pd.cut(portuguese['G3'], bins=bins, labels=labels)

print("-----------------------Head of Math Data Set-----------------------")
print(math.head())
print("-----------------------Head of Portuguese Data Set-----------------------")
print(portuguese.head())

math_x = math.iloc[:, :-3].values
math_y = math.iloc[:, -1].values
port_x = portuguese.iloc[:, :-3].values
port_y = portuguese.iloc[:, -1].values


math_x_train,math_x_test,math_y_train,math_y_test = train_test_split(math_x,math_y,test_size=0.28,random_state=42,stratify=math_y)

print("-----------------------KNN Results-----------------------")
knn.knn(math_x_train, math_x_test, math_y_train, math_y_test)

print("-----------------------Decision Tree Results-----------------------")
dt.dt(math_x_train, math_x_test, math_y_train, math_y_test)
