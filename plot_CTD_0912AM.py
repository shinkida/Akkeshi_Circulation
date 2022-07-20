# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 12:26:53 2021

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

a = pd.read_csv('E01_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D01=A[:,0]
T01=A[:,1]
S01=A[:,2]

a = pd.read_csv('E02_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D02=A[:,0]
T02=A[:,1]
S02=A[:,2]

a = pd.read_csv('E03_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D03=A[:,0]
T03=A[:,1]
S03=A[:,2]

a = pd.read_csv('E04_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D04=A[:,0]
T04=A[:,1]
S04=A[:,2]

a = pd.read_csv('E05_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D05=A[:,0]
T05=A[:,1]
S05=A[:,2]

a = pd.read_csv('E06_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D06=A[:,0]
T06=A[:,1]
S06=A[:,2]

a = pd.read_csv('E07_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D07=A[:,0]
T07=A[:,1]
S07=A[:,2]

a = pd.read_csv('E08_0912.Csv',skiprows=6, encoding="shift-jis")
A = a.to_numpy()
D08=A[:,0]
T08=A[:,1]
S08=A[:,2]

Depth=D02
Salt=np.empty([73,8])*np.nan
Salt[0:40,0]=S01
Salt[0:73,1]=S02
Salt[0:69,2]=S03
Salt[0:64,3]=S04
Salt[0:58,4]=S05
Salt[0:55,5]=S06
Salt[0:45,6]=S07
Salt[0:14,7]=S08

im=plt.contourf(-np.arange(0,8,1),-Depth,Salt,cmap=mymap,vmin=27.5,vmax=32.5,levels=clevels,extend='both')
plt.contour(-np.arange(0,8,1),-Depth,Salt,levels=clevels,colors='k')
plt.ylim([-8,0])
plt.yticks(np.arange(-8,2,2))
plt.colorbar(im,orientation='vertical',ticks=cticks)
