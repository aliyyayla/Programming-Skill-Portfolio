#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:03:34 2023

@author: aliyya
"""
"""
Chapter 1 Exercise 5: Compute the Area of Circle
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi
r= float(input("input the radius of the circle : "))
print ("Area=" ,pi * r**2)