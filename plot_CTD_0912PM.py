# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:31:07 2021

@author: shink
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

greys=cm.get_cmap('Greys_r',11)
colors0=greys(np.linspace(0,1,11))
colors00=np.vstack((colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],colors0[4],
                    colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],colors0[5],
                    colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],colors0[6],
                    colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],colors0[7],
                    colors0[8],colors0[8],colors0[8],colors0[8],colors0[8],colors0[8],colors0[8],colors0[8],colors0[8],colors0[8]))

bwr=cm.get_cmap('bwr',71)
colors1 = bwr(np.linspace(0,1,71))

Greens_r=cm.get_cmap('YlGn_r',31)
colors2 = Greens_r(np.linspace(0,1,31))

bwr_r=cm.get_cmap('bwr_r',21)
colors3 = bwr_r(np.linspace(0,1,21))

colors = np.vstack((colors1[9:34:1], colors2[9:29:1], colors3[5:10:1]))
mymap = ListedColormap(colors)

clevels=np.arange(27.5,32.51,0.1)
cticks=np.arange(28.0,33,1)

a = pd.read_csv('D01_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D04=A[:,0]
T04=A[:,1]
S04=A[:,2]

a = pd.read_csv('D01A_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D05=A[:,0]
T05=A[:,1]
S05=A[:,2]

a = pd.read_csv('D02_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D07=A[:,0]
T07=A[:,1]
S07=A[:,2]

a = pd.read_csv('D03_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D08=A[:,0]
T08=A[:,1]
S08=A[:,2]

a = pd.read_csv('D04_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D09=A[:,0]
T09=A[:,1]
S09=A[:,2]

a = pd.read_csv('D05_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D10=A[:,0]
T10=A[:,1]
S10=A[:,2]

a = pd.read_csv('D06_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D11=A[:,0]
T11=A[:,1]
S11=A[:,2]

a = pd.read_csv('D07_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D12=A[:,0]
T12=A[:,1]
S12=A[:,2]

Depth=D07

Salt=np.empty([111,12])*np.nan
Salt[0:61,3]=S04  #D01
Salt[0:34,4]=S05  #D01A
Salt[0:111,6]=S07 #D02
Salt[0:14,7]=S08  #D03
Salt[0:26,8]=S09  #D04
Salt[0:46,9]=S10  #D05
Salt[0:62,10]=S11 #D06
Salt[0:68,11]=S12 #D07

SaltM=np.empty([111,8])*np.nan
SaltM[:,0]=Salt[:,3]
SaltM[:,1]=Salt[:,4]
SaltM[:,2]=Salt[:,6]
SaltM[:,3]=Salt[:,7]
SaltM[:,4]=Salt[:,8]
SaltM[:,5]=Salt[:,9]
SaltM[:,6]=Salt[:,10]
SaltM[:,7]=Salt[:,11]

im=plt.contourf(-np.arange(0,8,1),-Depth,SaltM,cmap=mymap,vmin=27.5,vmax=32.5,levels=clevels,extend='both')
plt.contour(-np.arange(0,8,1),-Depth,SaltM,levels=clevels,colors='k')
plt.ylim([-8,0])
plt.yticks(np.arange(-8,2,2))
plt.colorbar(im,orientation='vertical',ticks=np.arange(28.0,32.5,1.0))
