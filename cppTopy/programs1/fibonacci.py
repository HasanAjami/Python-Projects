# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:12:32 2022

@author: 123
"""

def fibonacci(entries):
    result = [None] * entries
    
    result[0] = 0
    result[1] = 1
    
    for i in range(2, len(result)):
        result[i] = result[i-2] + result[i-1]
        
    return result
