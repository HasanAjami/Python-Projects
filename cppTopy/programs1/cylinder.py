# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:16:42 2022

@author: 123
"""

from circle import Circle
import math

class Cylinder():
    def __init__(self, radius, height):
        self.__m_height = height
        
        self.myCircle = Circle(radius)
    def volume(self):
        return math.pi* (self.myCircle._m_radius**2) * self.__m_height
    