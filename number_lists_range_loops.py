#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:52:11 2023

@author: nooblost
"""

for value in range(1,6):
    print(value)
    
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
   squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)] #list comprehensions
print(squares)

#combining multiple lines of code into one
