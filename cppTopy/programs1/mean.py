# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:56:50 2022

@author: 123
"""

def mean_even_numbers(list_input):
    m_sum = 0
    n = 0
    
    for i in list_input:
        if((i%2) == 0):
            m_sum = m_sum +i
            n = n+1
            
    if (n == 0):
        return 0
    else:
        return m_sum/n
    