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
    #for i in range(0,3*array_length):
    #    for j in range (0,3*array_length):
    #        if mask[i,j]==True:
    #            try:
    #                ang=np.arctan2((center-i),(j-center))
    #                angle[i,j]=ang
    #                if i>center:
    #                    angle[i,j]=ang+2*np.pi
    #
    #            except ZeroDivisionError as error:
    #                if center-i>=0:
    #                    angle[i,j]=np.pi/2
    #                elif center-i<0:
    #                    angle[i,j]=np.pi/2



    masque1=create_circular_mask(3*array_length, 3*array_length,None,inner )
    masque2=create_circular_mask(3*array_length, 3*array_length,None,outer)
    masque_tot=~(masque1) & masque2
    #viridis = cm.get_cmap('viridis', 256)

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
    #img = Image.fromarray(data, 'RGB')
    # img.save('my.png')


#            #premiere ligne, toute colonne
#            if (i >= 0 and i < centerDown) :
#                   # PUT DATA_UP HERE !!!!
#                if(masque_tot[i,j]==True):
#                    try:
#                        ang=np.arctan2((center-i),(j-center))
#                        angle[i,j]=ang
#                        if i>center:
#                            angle[i,j]=ang+2*np.pi
#
#                    except ZeroDivisionError as error:
#                        if center-i>=0:
#                            angle[i,j]=np.pi/2
#                        elif center-i<0:
#                            angle[i,j]=np.pi/2
#
#                    minimum = np.min(abs(angle[i,j]-angle_array));
#                    index_angle = np.where(abs(angle[i,j]-angle_array) == minimum)[0];
#                    data[i,j]=abs(v1[j])
#                else:
#                    #data[i,j]=int(viridis(0)[0]);
#                    data[i,j]= 0
#
#
#            #ligne du centre
#            elif (i >= centerDown and i < centerUp) :
#                #premieres colonnes
#                 # PUT DATA_LEFT HERE !!!!
#                if (j >=0 and j<=array_length) :
#                    data[i,j]=abs(v1[j]+v2[j])
#
#                 # colonnes du centre
#                elif(masque_tot[i,j]==True and i>=center):
#                    try:
#                        ang=np.arctan2((center-i),(j-center))
#                        angle[i,j]=ang
#                        if i>center:
#                            angle[i,j]=ang+2*np.pi
#
#                    except ZeroDivisionError as error:
#                        if center-i>=0:
#                            angle[i,j]=np.pi/2
#                        elif center-i<0:
#                            angle[i,j]=np.pi/2
#
#                      # PUT DATA_Down HERE !!!!
#                    minimum = np.min(abs(angle[i,j]-angle_array));
#                    index_angle = np.where(abs(angle[i,j]-angle_array) == minimum)[0];
#                    data[i,j]=abs(v2[index_angle+array_length])
#
#                elif(masque_tot[i,j]==True and i<center):
#
#                    try:
#                        ang=np.arctan2((center-i),(j-center))
#                        angle[i,j]=ang
#                        if i>center:
#                            angle[i,j]=ang+2*np.pi
#
#                    except ZeroDivisionError as error:
#                        if center-i>=0:
#                            angle[i,j]=np.pi/2
#                        elif center-i<0:
#                            angle[i,j]=np.pi/2
#
#                    # PUT DATA_UpHERE !!!!
#                    minimum = np.min(abs(angle[i,j]-angle_array));
#                    index_angle = np.where(abs((angle[i,j]-angle_array)) == minimum)[0];
#                    data[i,j]=abs(v1[index_angle+array_length])
#
#                elif(j >=2*array_length):
#                       # PUT DATA_Rigth HERE !!!!
#                    data[i,j] = abs(v1[j] + v2[j])
#
#                else:
##                    data[i,j]=int(viridis(0)[0]);
#                    data[i,j]=0
#
#            #ligne fin
#            elif (i >= centerUp) :
#
#                if(masque_tot[i,j]==True):
#                    try:
#                        ang=np.arctan2((center-i),(j-center))
#                        angle[i,j]=ang
#                        if i>center:
#                            angle[i,j]=ang+2*np.pi
#
#                    except ZeroDivisionError as error:
#                         if center-i>=0:
#
#                             angle[i,j]=np.pi/2
#                         elif center-i<0:
#                             angle[i,j]=np.pi/2
#                      # PUT DATA_Down HERE !!!!
#                    minimum = np.min(abs(angle[i,j]-angle_array));
#                    index_angle = np.where(abs(angle[i,j]-angle_array) == minimum)[0];
#                    data[i,j]=abs(v2[index_angle+array_length])
#
#                else:
#                    #data[i,j]=int(viridis(0)[0]);
#                    data[i,j]=0
#
#
#            else:
#                #data[i,j]=int(viridis(0)[0]);
#                data[i,j]=0
#
#
#
#
#    #angle= np.linspace(0, math.pi, array_length, endpoint=True);
#    #x = outer*np.cos(angle);
#    #yInf_In=-1*inner*np.sin(angle);
#    #yInf_Out=-1*outer*np.sin(angle);
#    #ySup_out=outer*np.sin(angle);
#    #ySup_In=inner*np.sin(angle);
#
#    #for i in range(0,3*array_length) :
#    #    for j in range(0,3*array_length) :
#    #            if (j >=0 and j<array_length) :
    #                data[i,j,0]=int(viridis(100)[0]);
    #                data[i,j,1]=int(viridis(100)[1]);
    #                data[i,j,2]=int(viridis(100)[2]);
    #
    #            elif  (j >2*array_length and j<=3*array_length) :
    #                data[i,j,0]=int(viridis(250)[0]);
    #                data[i,j,1]=int(viridis(250)[1]);
    #                data[i,j,2]=int(viridis(250)[2]);

    #        if (i > centerDown and i < centerUp) :
