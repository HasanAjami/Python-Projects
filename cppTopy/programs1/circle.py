# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:13:43 2022

@author: 123
"""
import math

class Circle:
    def __init__(self, radius):
        self._m_radius = radius
        
    def base_area(self):
        return math.pi*(self._m_radius**2)
