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
        for job in row:
            if (job != "teacher" and job != "health" and job != "services" and job != "at_home" and job != "other"):
                print(job)
                
    for reason in data.iloc[:, 10]:
        if (reason != "home" and reason != "other" and reason != "reputation" and reason != "course"):
            print(reason)
            
    for guardian in data.iloc[:, 11]:
        if (guardian != "mother" and guardian != "father" and guardian != "other"):
            print(guardian)
            
    for index, row in data.iloc[:, 12:14].iterrows():
        for rng1_4 in row:
            if (not isinstance(rng1_4, int) or rng1_4 < 1 or rng1_4 > 4):
                print(rng1_4)
    
    for failure in data.iloc[:, 14]:
        if (not isinstance(failure, int) or failure < 0 or failure > 4):
            print(failure)
        
    for index, row in data.iloc[:, 15:23].iterrows():
        for binary in row:
            if (binary != "yes" and binary != "no"):
                print(binary)
                
    for index, row in data.iloc[:, 23:29].iterrows():
        for rng1_5 in row:
            if (not isinstance(rng1_5, int) or rng1_5 < 1 or rng1_5 > 5):
                print(prnt_educ)
    
    for absences in data.iloc[:, 29]:
        if (not isinstance(absences, int) or absences < 0 or absences > 93):
            print(absences)
                