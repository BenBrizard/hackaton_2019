import matplotlib.pyplot as plt
#plt.rcParams['animation.ffmpeg_path'] = r"C:\Users\Benoit Brizard\Anaconda3\pkgs\ffmpeg-4.2-h6538335_0\Library\bin\ffmpeg.exe"
from matplotlib import animation
import numpy as np

from PIL import Image
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
def create_circular_mask(h, w, center=None, radius=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask


def two_D_plot(v1,v2,length) :
    array_length=int(length//3);
    largeur=int(array_length//5);
    center=int(3*array_length//2);
    centerUp=int(3*array_length//2+largeur);
    centerDown=int(3*array_length//2-largeur)
    outer = int(array_length//2);
    inner = outer - largeur;
    data = np.zeros((3*array_length, 3*array_length))

    angle_array=np.linspace(0,2*np.pi,2*array_length);

    angle=np.zeros((3*array_length,3*array_length))
    masque1=create_circular_mask(3*array_length, 3*array_length,None,inner )
    masque2=create_circular_mask(3*array_length, 3*array_length,None,outer)
    masque_tot=~(masque1) & masque2
  

#premier rectangle
    for i in range(centerDown,centerUp) :
        for j in range(0,array_length) :
            data[i,j]=abs(v1[j]+v2[j]);
#2e rectangle
    for i in range(centerDown,centerUp) :
        for j in range(2*array_length,3*array_length) :
            data[i,j]=abs(v1[j]+v2[j]);

#cercle
    for i in range(array_length,2*array_length) :
        for j in range(array_length,2*array_length) :
            if masque_tot[i,j]==True:
                try:
                    ang=np.arctan2((center-i),(j-center))
                    angle[i,j]=ang
                    if i>center:
                        angle[i,j]=ang+2*np.pi

                except ZeroDivisionError as error:
                    if center-i>=0:
                        angle[i,j]=np.pi/2
                    elif center-i<0:
                        angle[i,j]=np.pi/2
                minimum = np.min(abs(angle[i,j]-angle_array));
                index_angle = np.where(abs(angle[i,j]-angle_array) == minimum)[0];
            
                if(index_angle<=array_length):
                    index_angle=int(len(angle_array)//2)-index_angle;
                else:
                    index_angle=index_angle-int(len(angle_array)//2);


                if(i>center):
                    data[i,j]=abs(v2[index_angle+array_length])
                else:
                    data[i,j]=abs(v1[index_angle+array_length])

    return data