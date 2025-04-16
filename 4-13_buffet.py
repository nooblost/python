#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:19:22 2023

@author: nooblost
"""

buffet = 'eggs', 'sausages', 'bacon', 'pasta', 'toast'
print("Buffet foods")
for buffet in buffet:
    print(buffet)

#buffet[0] = 'scrambled eggs'
#print(buffet)
#these two lines attempt to modify the tuple
#it's not possible to modify a tuple
#must rewrite the whole thing

buffet = 'scrambled eggs', 'sausages', 'bacon', 'pasta', 'toast'
print("\nNew Buffet foods")
for buffet in buffet:
    print(buffet)