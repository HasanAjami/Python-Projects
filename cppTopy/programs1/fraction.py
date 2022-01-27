# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:23:38 2022

@author: 123
"""

class Fraction:
    def __init__(self, num, denom):
        self.__m_num = num
        self.__m_denom = denom
        
    def get_num(self):
        return self.__m_num
    
    def get_denom(self):
        return self.__m_denom
    
    def operator(self,rhs):
        num = self.__m_num*rhs.__m_denom + rhs.__m_num*self.__m_denom
        denom = self.__m_denom * rhs.__m_denom
        
        return Fraction(num, denom)
