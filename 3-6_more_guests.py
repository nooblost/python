#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:57:20 2023

@author: nooblost
"""

guests = ['abbie', 'gilgamesh', 'mom']

cannot_attend = 'gilgamesh'
guests.remove(cannot_attend)
guests.append("ruben")
message_a = f"I would like to invite you to dinner, {guests[0].title()}."
message_b = f"I would like to invite you to dinner, {guests[1].title()}."
message_c = f"I would like to invite you to dinner, {guests[2].title()}."
invite = f"{message_a}\n{message_b}\n{message_c}"
print(f"\n{cannot_attend.title()} can't make it to the dinner.")
print(invite)

new_table = "I found a bigger table."
print(new_table)

guests.insert(0, 'nicole')
guests.insert(1, 'tong')
guests.append('ciaran')

for x in guests:
    print(f"I would like to invite you to dinner, {x.title()}")