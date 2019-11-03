#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:37:12 2019

@author: paulxing
"""


import numpy as np

import math
import matplotlib.pyplot as plt
def create_circular_mask(h, w, center=None, radius=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask






exemple=10*np.ones((200,200))


mask1=create_circular_mask(200, 200, None, 50)

mask3=~mask1
mask2=create_circular_mask(200, 200, None, 75)
mask=(mask3) & (mask2)

exemple[mask] = 0



plt.imshow(exemple);
plt.colorbar()
plt.show()