#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:09:36 2023

@author: nooblost
"""

#slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first 3 players on our team:")
for player in players[:3]:
    print(player.title())
    
print("Three items from the middle of the list are:")
for player in players[1:4]:
    print(player.title())
    
print("The last three items in the list are:")
for player in players[-3:]:
    print(player.title())