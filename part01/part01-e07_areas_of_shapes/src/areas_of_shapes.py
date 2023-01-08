#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        shape = str(input('Choose a shape (triangle, rectangle, circle):'))
        if shape == '':
            break
        if shape not in ('triangle', 'rectangle', 'circle'):
            print('Unknown shape!')
        elif shape == 'triangle':
            base = float(input('Give the base of the triangle: '))
            height = float(input('Give the height of the triangle: '))
            print(f'The area is {base * height / 2:.6f}')
        elif shape == 'rectangle':
            width = float(input('Give the width of the rectangle: '))
            height = float(input('Give the height of the rectangle: '))
            print(f'The area is {width * height:.6f}')
        else :
            radius = float(input('Give the radius of the circle: '))
            print(f'The area is {math.pi * radius ** 2:.6f}')


if __name__ == "__main__":
    main()
