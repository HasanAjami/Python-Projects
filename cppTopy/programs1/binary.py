# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:19:36 2022

@author: 123
"""

def binary_to_int(binary):
    m_sum = 0
    count = 0
    
    for i in binary:
        
        m_sum += (2**count) * i
        count += 1
        
    return m_sum