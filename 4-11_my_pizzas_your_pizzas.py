#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:38:35 2023

@author: nooblost
"""

my_pizzas = ['margarita', 'pepperoni', 'hawaiian']
friend_pizzas = my_pizzas[:]

print(my_pizzas)
print(friend_pizzas)

my_pizzas.append('mushroom parma ham')
friend_pizzas.append('seafood pizza')


print(my_pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for pizzas in my_pizzas:
	print(pizzas.title())

print("\nMy friends' favorite pizzas are:")
for pizzas in friend_pizzas:
	print(pizzas.title())
