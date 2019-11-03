import matplotlib.pyplot as plt
plt.rcParams['animation.ffmpeg_path'] = r"C:\Users\Benoit Brizard\Anaconda3\pkgs\ffmpeg-4.2-h6538335_0\Library\bin\ffmpeg.exe"
from matplotlib import animation
import numpy as np
import math



array_length=1000;
nb_frames=100;
inner = 5.
outer =5.

angle= np.linspace(0, 2*math.pi, 1000, endpoint=True)

x = []
y = []
for i in range(0,array_length):
    x.append(math.cos(angle[i]));
    y.append(math.sin(angle[i]));

#yO = outer*np.sin(np.arccos(x/outer)) # x-axis values -> outer circle
#yI = inner*np.sin(np.arccos(x/inner)) # x-axis values -> inner circle (with nan's beyond circle)
#yI[np.isnan(yI)] = 0.                 # yI now looks like a boulder hat, meeting yO at the outer points
intensity=np.random.rand(array_length);
fig = plt.figure()
scat = plt.scatter(x,y,c=intensity,s=1)
#ax = plt.subplot(111)
#ax.fill_between(x, yI, yO, color="red")
#ax.fill_between(x, -yO, -yI, color="red")



def animate(i):
    print(i)
    intensity=np.random.rand(array_length);
    scat.set_array(intensity)
    return scat
#    if i<10 :
#        ax.fill_between(x, yI, yO, color="blue")
#        ax.fill_between(x, -yO, -yI, color="blue")
#        return ax
#    else:
#        ax.fill_between(x, yI, yO, color="red")
#        ax.fill_between(x, -yO, -yI, color="red")
#        return ax
        

anim = animation.FuncAnimation(fig,animate,nb_frames)
anim.save('monvideo.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()