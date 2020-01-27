#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:56:19 2020

@author: aims
"""
grades = [73, 67, 38, 33]

#def gradingStudents(grade):
#    g = grade 
#    if grade >= 38:
#        while g % 5 != 0:
#            g += 1
#        if (g - grade) < 3:
#            return (g)
#        else:
#            return grade
#    else:
#        return grade


def gradingStudents(grade):
    final_grade = []
    for i in grades:
        grade = i
        if i >= 38:
            while grade % 5!= 0:
                grade+=1
            if (grade - i) < 3:
                final_grade.append(grade)
            else:
                final_grade.append(i)
        else:
            final_grade.append(i)
    return final_grade
                
    
            
print(gradingStudents(grades))
