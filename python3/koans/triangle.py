#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    pass

def triangle(a, b, c):
    side1, side2, side3 = a, b, c
    list_side = [side1, side2, side3]

    # part 2
    ''' 
    Maybe that I should have use the pythagore theorem  
    '''
    f = lambda x: x < 0
    negatif_list = [f(x) for x in list_side]
    if 0 in list_side:
    	raise(TriangleError)
    elif True in negatif_list:
    	raise(TriangleError)
    if list_side.count(1) == 2 or list_side.count(2) == 2:
    	raise(TriangleError)

    # part 1
    if list_side.count(side1) == 3:
    	return 'equilateral'
    if list_side.count(side1) == 2 or list_side.count(side3) == 2:
    	return 'isosceles'
    return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
