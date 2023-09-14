# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:43:52 2023

@author: SERNi
"""

def clean_student_performance(data):
    indices_to_drop = []
    
    for index, school in data.iloc[:, 0].items():
        if (school != "GP" and school != "MS"):
            print("invalid school: "+ school)
            indices_to_drop.append(index)

    for index, sex in data.iloc[:, 1].items():
        if (sex != "F" and sex != "M"):
            print("invalid sex: " + sex )
            indices_to_drop.append(index)

    for index, age in data.iloc[:, 2].items():
        if (not isinstance(age, int) or age < 15 or age > 22):
            print(age)
            indices_to_drop.append(index)
            
    for index, address in data.iloc[:, 3].items():
        if (address != "U" and address != "R"):
            print("invalid address: " + address)
            indices_to_drop.append(index)
    
    for index, famsize in data.iloc[:, 4].items():
        if (famsize != "LE3" and famsize != "GT3"):
            print("invalid famsize: "+ famsize)
            indices_to_drop.append(index)
    
    for index, pstatus in data.iloc[:, 5].items():
        if (pstatus != "T" and pstatus != "A"):
            print("invalid pstatus: " + pstatus)
            indices_to_drop.append(index)
    
    for index, row in data.iloc[:, 6:8].iterrows():
        for prnt_educ in row:
            if (not isinstance(prnt_educ, int) or prnt_educ < 0 or prnt_educ > 4):
                indices_to_drop.append(index)

    for index, row in data.iloc[:, 8:10].items():
        for job in row:
            if (job != "teacher" and job != "health" and job != "services" and job != "at_home" and job != "other"):
                indices_to_drop.append(index)
                
    for index, reason in data.iloc[:, 10].items():
        if (reason != "home" and reason != "other" and reason != "reputation" and reason != "course"):
            print("invalid reason: " + reason)
            indices_to_drop.append(index)
            
    for index, guardian in data.iloc[:, 11].items():
        if (guardian != "mother" and guardian != "father" and guardian != "other"):
            print("invalid guardian: " + guardian)
            indices_to_drop.append(index)

    for index, row in data.iloc[:, 12:14].items():
        for rng1_4 in row:
            if (not isinstance(rng1_4, int) or rng1_4 < 1 or rng1_4 > 4):
                indices_to_drop.append(index)
    
    for index, failure in data.iloc[:, 14].items():
        if (not isinstance(failure, int) or failure < 0 or failure > 4):
            print("invalid failure: " + failure)
            indices_to_drop.append(index)
        
    for index, row in data.iloc[:, 15:23].items():
        for binary in row:
            if (binary != "yes" and binary != "no"):
                indices_to_drop.append(index)
                
    for index, row in data.iloc[:, 23:29].items():
        for rng1_5 in row:
            if (not isinstance(rng1_5, int) or rng1_5 < 1 or rng1_5 > 5):
                indices_to_drop.append(index)
    
    for index, absences in data.iloc[:, 29].items():
        if (not isinstance(absences, int) or absences < 0 or absences > 93):
            indices_to_drop.append(index)

    for index, row in data.iloc[:, 30:33].items():
        for prnt_educ in row:
            if prnt_educ not in range(0, 21):
                indices_to_drop.append(index)
                
    print("\nindices to drop")
    print(indices_to_drop)
    data = data.drop(indices_to_drop)
    
    print("\nfinal data:  ")
    print(indices_to_drop)
