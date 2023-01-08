#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    x,y = a.shape[:2]
    return ((x-1)/2,(y-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    x, y = a.shape[:2]
    a = np.zeros((x, y, 2))
    a[..., 0], a[..., 1] = np.arange(x)[:, None], np.arange(y)         
    b = np.full((x, y, 2), fill_value=center(a))
    return np.linalg.norm(a-b, axis=-1)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range  [tmin,tmax]."""
    image = np.copy(a)
    min, max = np.amin(image) , np.amax(image)
    if (max - min) == 0:
        return np.zeros(np.shape(image))
    return (((tmax-tmin) * (image-min)) / (max - min)) + tmin

def radial_mask(a):
    return 1 - scale(radial_distance(a), 0, 1)

def radial_fade(a):
    return a * radial_mask(a)[:, :, None]

def main():
    painting=plt.imread("src/painting.png")
    mask = radial_mask(painting)
    faded = radial_fade(painting)
    plt.subplot(3, 1, 1)
    plt.imshow(painting)
    plt.subplot(3, 1, 2)
    plt.imshow(mask)
    plt.subplot(3, 1, 3)
    plt.imshow(faded)
    plt.show()
    pass

if __name__ == "__main__":
    main()
