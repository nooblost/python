#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 18:00:18 2023

@author: nooblost
"""

#Chapter 3 - Introducing Lists
#square brackets [] are for lists, good to give them plural names

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0]) #lists start from 0, not 1
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[-1].title()) #-1 goes to last item on list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)