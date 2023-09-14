# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:43:52 2023

@author: SERNi
"""

def clean_student_performance(data):
    for school in data.iloc[:, 0]:
        if (school != "GP" and school != "MS"):
            print(school)
            
    for sex in data.iloc[:, 1]:
        if (sex != "F" and sex != "M"):
            print(sex)
    
    for age in data.iloc[:, 2]:
        if (not isinstance(age, int) or age < 15 or age > 22):
            print(age)
            
    for address in data.iloc[:, 3]:
        if (address != "U" and address != "R"):
            print(address)
    
    for famsize in data.iloc[:, 4]:
        if (famsize != "LE3" and famsize != "GT3"):
            print(famsize)
    
    for pstatus in data.iloc[:, 5]:
        if (pstatus != "T" and pstatus != "A"):
            print(pstatus)
    
    for index, row in data.iloc[:, 6:8].iterrows():
        for prnt_educ in row:
            if (not isinstance(prnt_educ, int) or prnt_educ < 0 or prnt_educ > 4):
                print(prnt_educ)
                
    for index, row in data.iloc[:, 8:10].iterrows():
        for prnt_educ in row:
            None