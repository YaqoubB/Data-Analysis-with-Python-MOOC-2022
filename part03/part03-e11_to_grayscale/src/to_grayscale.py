
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_red(image):
    return image * np.array([1, 0, 0])

def to_green(image):
    return image * np.array([0, 1, 0])

def to_blue(image):
    return image * np.array([0, 0, 1])

def to_grayscale(image):
    weights=np.array([0.2126, 0.7152, 0.0722]) 
    result = np.dot(image, weights)     
    plt.imshow(result) 
    plt.show()
    return result

def main():
    image=plt.imread("src/painting.png")
    plt.imshow(image) 
    fig, (ax1, ax2, ax3) = plt.subplots(3)
    ax1.imshow(to_red(image))
    ax2.imshow(to_green(image))
    ax3.imshow(to_blue(image))
    plt.show()
    pass

if __name__ == "__main__":
    main()
    to_grayscale(plt.imread("painting.png"))

