#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:37:12 2019

@author: paulxing
"""


import numpy as np
import random
import math
import matplotlib.pyplot as plt
import copy




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


angle=np.zeros((200,200))
for i in range(0,200):
    for j in range (0,200):
        if mask[i,j]==True:
            try:
                ang=np.arctan2((100-i),(j-100))
                angle[i,j]=ang
                if i>100:
                    angle[i,j]=ang+2*np.pi
                    
            except ZeroDivisionError as error:
                if 100-i>=0:
                    angle[i,j]=np.pi/2
                elif 100-i<0:
                    angle[i,j]=np.pi/2
        
plt.imshow(angle);
cbar=plt.colorbar()
intensity=np.zeros((200,200))
plt.show()                    
color=np.random.rand(26)  
color=np.linspace(25,0,26)                  
vec_intervalle=np.linspace(0,2*np.pi,26)
for i in range(0,25):
    mask1=angle <= vec_intervalle[i+1]
    mask2=angle >= vec_intervalle[i]
    mask=(mask1) & (mask2)
    intensity[mask]=color[i]


#intensity=np.zeros((200,200))
#for i in range(0,200):
#    for j in range (0,200):
#        if mask[i,j]==True:
#            intensity[i,j]=random.randint(0, 10)           
         

            

plt.imshow(intensity);
cbar=plt.colorbar()

plt.show()

