# Enter you module contents here

'''This module contains functions for calculating the area and hypothenuse of a right triangle'''
__author__ = "Author Name x"
__version__ = "1.0"

def hypothenuse(a,b):
    '''Returns the hypothenuse of a right triangle when given the lengths of the other two sides'''
    return (a**2 + b**2)**0.5

def area(a,b):
    '''Returns the area of a right triangle when given the height and breadth'''
    return (a*b)/2

#print("Using __doc__:")
#print(hypothenuse.__doc__)
#print(__version__)

