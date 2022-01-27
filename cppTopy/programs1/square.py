# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:47:38 2022

@author: 123
"""
def sum_of_squares(entries):
    result = [None] * entries
    result[0] = 0;
    
    for i in range(1, len(result)):
        result[i] = result[i-1]+(i*i)
    
    return result

#Anwendungsbeispiel:
#print(sum_of_squares(10))
    
    
    
