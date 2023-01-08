#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(a[:,0], a[:,1])
    ax2.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()
    pass

def main():
    pass

if __name__ == "__main__":
    main()

