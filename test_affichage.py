import numpy as np
#import cv2
#from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

def matriceIntensite(xx,yy,psi1,psi2) :
    data = np.zeros((xx,yy))
    maximum = 5
    for i in range(maximum,xx-maximum):
        for j in range(maximum,yy-maximum):

            if (j == yy//2 and i <= xx//3):
                for k in range(1,maximum):
                    data[j,i] = abs(psi1[i] + psi2[i])
                    data[j,i+k] = abs(psi1[i] + psi2[i])
                    data[j,i-k] = abs(psi1[i] + psi2[i])
                    data[j+k,i] = abs(psi1[i] + psi2[i])
                    data[j-k,i] = abs(psi1[i] + psi2[i])
            elif (j == -i + (yy//2 + yy//3) and j <= yy/2 and i >= xx//3 and i <= xx//2):
                for k in range(1,maximum):
                    data[j,i] = abs(psi1[i])
                    data[j,i+k] = abs(psi1[i])
                    data[j,i-k] = abs(psi1[i])
                    data[j+k,i] = abs(psi1[i])
                    data[j-k,i] = abs(psi1[i])
            elif (j == i + (yy//2 - yy//3) and j >= yy/2 and i >= xx//3 and i <= xx//2):
                for k in range(1,maximum):
                    data[j,i] = abs(psi2[i])
                    data[j,i+k] = abs(psi2[i])
                    data[j,i-k] = abs(psi2[i])
                    data[j+k,i] = abs(psi2[i])
                    data[j-k,i] = abs(psi2[i])
            elif (i >= xx//2 and i <= 2*xx//3 and j <= yy//2 and j == i + (yy//2 - 2*yy//3)):
                for k in range(1,maximum):
                    data[j,i] = abs(psi1[i])
                    data[j,i+k] = abs(psi1[i])
                    data[j,i-k] = abs(psi1[i])
                    data[j+k,i] = abs(psi1[i])
                    data[j-k,i] = abs(psi1[i])
            elif(i >= xx//2 and i <= 2*xx//3 and j >= yy//2 and j == -i + (yy//2 + 2*yy//3)):
                for k in range(1,maximum):
                    data[j,i] = abs(psi2[i])
                    data[j,i+k] = abs(psi2[i])
                    data[j,i-k] = abs(psi2[i])
                    data[j+k,i] = abs(psi2[i])
                    data[j-k,i] = abs(psi2[i])
            elif(j == yy//2 and i >= 2*xx//3):
                for k in range(1,maximum):
                    data[j,i] = abs(psi1[i] + psi2[i])
                    data[j,i+k] = abs(psi1[i] + psi2[i])
                    data[j,i-k] = abs(psi1[i] + psi2[i])
                    data[j+k,i] = abs(psi1[i] + psi2[i])
                    data[j-k,i] = abs(psi1[i] + psi2[i])
            else:
                data[j,i] = 0

    return data
