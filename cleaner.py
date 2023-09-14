# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:43:52 2023

@author: SERNi
"""

def clean_student_performance(data):
    for index, school in data.iloc[:, 0].items():
        if (school != "GP" and school != "MS"):
            print("invalid school: "+ school)
            data = data.drop(index)

    for index, sex in data.iloc[:, 1].items():
        if (sex != "F" and sex != "M"):
            print("invalid sex: " + sex )
            data = data.drop(index)

    # for index, age in data.iloc[:, 2].items():
    #     if (not isinstance(age, int)):
    #         try:
    #             data.loc[index, "age"] = int(age)
    #         except:
    #             data = data.drop(index)
    #     elif (age < 15 or age > 22):
    #         print(age)
    #         data = data.drop(index)
            
    for index, address in data.iloc[:, 3].items():
        if (address != "U" and address != "R"):
            print("invalid address: " + address)
            data = data.drop(index)
    
    for index, famsize in data.iloc[:, 4].items():
        if (famsize != "LE3" and famsize != "GT3"):
            print("invalid famsize: "+ famsize)
            data = data.drop(index)
    
    for index, pstatus in data.iloc[:, 5].items():
        if (pstatus != "T" and pstatus != "A"):
            print("invalid pstatus: " + pstatus)
            data = data.drop(index)
    
    for index, row in data.iloc[:, 6:8].iterrows():
        for prnt_educ in row:
            print(f"{row}")
        # print(data.iloc[:, 6:8])
        # for prnt_educ in row:
        #     if (not isinstance(prnt_educ, int) or prnt_educ < 0 or prnt_educ > 4):
        #         print("invalid prnt_educ: " + prnt_educ)
        #         data = data.drop(index)

    # for index, row in data.iloc[:, 8:10].items():
    #     for job in row:
    #         if (job != "teacher" and job != "health" and job != "services" and job != "at_home" and job != "other"):
    #             print(job)
                
    for index, reason in data.iloc[:, 10].items():
        if (reason != "home" and reason != "other" and reason != "reputation" and reason != "course"):
            print(reason)
            data = data.drop(index)
            
    for index, guardian in data.iloc[:, 11].items():
        if (guardian != "mother" and guardian != "father" and guardian != "other"):
            print(guardian)
            data = data.drop(index)

    # for index, row in data.iloc[:, 12:14].items():
    #     for rng1_4 in row:
    #         if (not isinstance(rng1_4, int) or rng1_4 < 1 or rng1_4 > 4):
    #             print(rng1_4)
    #             data = data.drop(index)
    
    for index, failure in data.iloc[:, 14].items():
        if (not isinstance(failure, int) or failure < 0 or failure > 4):
            print(failure)
            data = data.drop(index)
        
    # for index, row in data.iloc[:, 15:23].items():
    #     for binary in row:
    #         if (binary != "yes" and binary != "no"):
    #             print(binary)
    #             data = data.drop(index)
                
    # for index, row in data.iloc[:, 23:29].items():
    #     for rng1_5 in row:
    #         if (not isinstance(rng1_5, int) or rng1_5 < 1 or rng1_5 > 5):
    #             print(prnt_educ)
    #             data = data.drop(index)
    
    for index, absences in data.iloc[:, 29].items():
        if (not isinstance(absences, int) or absences < 0 or absences > 93):
            print(absences)
            data = data.drop(index)

    # for index, row in data.iloc[:, 30:33].items():
    #     for prnt_educ in row:
    #         if prnt_educ not in range(0, 21):
    #             print(prnt_educ)
    #             data = data.drop(index)
    print("\n\nfinal data:  ")
    print(data)
