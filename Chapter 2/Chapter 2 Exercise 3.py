#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:44:12 2023

@author: aliyya
"""

"""
Chapter 2 Exercise 3: Stripping Names
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

fullname = "\t Aliyya Bohol \n"
print("Unmodified:")
print(fullname)

print("\nUsing lstrip():")
print(fullname.lstrip())

print("\nUsing rstrip():")
print(fullname.rstrip())

print("\nUsing strip():")
print(fullname.strip())
