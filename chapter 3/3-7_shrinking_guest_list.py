#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:09:10 2023

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


print("It turns out the table isn't arriving on time, I can only invite two people.")


popped = guests.pop()
print(f"Sorry, {popped.title()}, I can't invite you to the dinner.")

popped = guests.pop()
print(f"Sorry, {popped.title()}, I can't invite you to the dinner.")

popped = guests.pop(0)
print(f"Sorry, {popped.title()}, I can't invite you to the dinner.")

popped = guests.pop(0)
print(f"Sorry, {popped.title()}, I can't invite you to the dinner.")

print(f"Hi, {guests[0].title()} and {guests[1].title()}, you are still invited for the dinner, hope to see you there!")

del guests[0]
del guests[0]
print(guests)