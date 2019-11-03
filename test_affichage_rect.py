import numpy as np
import matplotlib.pyplot as plt

def matriceIntensite(xx,yy,psi1,psi2) :
    data=np.zeros((xx,yy))

    for i in range(yy//3,2*yy//3):
        for j in range(0,xx//3):
            data[i,j] = abs(psi1[j] + psi2[j])
    for i in range(0,yy//3):
        for j in range(xx//3,2*xx//3):
            data[i,j] = abs(psi1[j])
    for i in range(2*yy//3,yy):
        for j in range(xx//3,2*xx//3):
            data[i,j] = abs(psi2[j])
    for i in range(yy//3,2*yy//3):
        for j in range(2*xx//3,xx):
            data[i,j] = abs(psi1[j] + psi2[j])
    return data
#
#xx = 1500
#yy = 1500
#ps1 = np.linspace(0,1,1500)
#ps2 = np.linspace(0,1,1500)
#data = matriceIntensite(xx,yy,ps1,ps2)
#plt.pcolormesh(data)
#plt.show()
