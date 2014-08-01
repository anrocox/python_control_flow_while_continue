#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

How to working the continue statement in while loop in Python?

¿Cómo funciona la sentencia continue en el ciclo while de Python?
'''

#the continue statement returns the control to the beginning of the while loop

#create a integer
n = 0

#iterates whilst the value of n is less than 10
while n < 10:

    #adds 1 to value n
    n += 1
    print('n = ' + str(n))

    #checks if the remainder of the division by two is equal to 0
    #if n is a odd number moves the control back to the top of the loop
    if n % 2 != 0:
        continue

    print('{} is a even number'.format(n))
    #adds 2 to value n
    n += 2
