# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:29:17 2021

@author: kida
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

# Use custom colormap function from Earle
def custom_div_cmap(numcolors=11, name='custom_div_cmap',
                    mincol='blue', midcol='white', maxcol='red'):
    """ Create a custom diverging colormap with three colors
    
    Default is blue to white to red with 11 colors.  Colors can be specified
    in any way understandable by matplotlib.colors.ColorConverter.to_rgb()
    """

    from matplotlib.colors import LinearSegmentedColormap 
    
    cmap = LinearSegmentedColormap.from_list(name=name, 
                                             colors =[mincol, midcol, maxcol],
                                             N=numcolors)
    return cmap

            
a = pd.read_csv('0912am/0912am.TcoE',skiprows=39)
A = a.to_numpy()
lon=A[:,4]
lat=A[:,3]
u=A[:,7]
lon=np.array(lon, dtype=float)
lat=np.array(lat, dtype=float)
u=np.array(u, dtype=float)
u[u==9999]=np.nan

a = pd.read_csv('0912am/0912am.TcoN',skiprows=39)
A = a.to_numpy()
v=A[:,7]
v=np.array(v, dtype=float)
v[v==9999]=np.nan

a = pd.read_csv('0912am/0912am.TcoV',skiprows=39)
A = a.to_numpy()
Us=A[:,7]
Us=np.array(Us, dtype=float)
Us[Us==9999]=np.nan

a = pd.read_csv('0912pm/0912pm.TcoE',skiprows=39)
A = a.to_numpy()
lon2=A[:,4]
lat2=A[:,3]
u2=A[:,7]
lon2=np.array(lon2, dtype=float)
lat2=np.array(lat2, dtype=float)
u2=np.array(u2, dtype=float)
u2[u2==9999]=np.nan

a = pd.read_csv('0912pm/0912pm.TcoN',skiprows=39)
A = a.to_numpy()
v2=A[:,7]
v2=np.array(v2, dtype=float)
v2[v2==9999]=np.nan

a = pd.read_csv('0912pm/0912pm.TcoV',skiprows=39)
A = a.to_numpy()
Us2=A[:,7]
Us2=np.array(Us2, dtype=float)
Us2[Us2==9999]=np.nan

a = pd.read_csv('0913am/0913am.TcoE',skiprows=39)
A = a.to_numpy()
lon3=A[:,4]
lat3=A[:,3]
u3=A[:,7]
lon3=np.array(lon3, dtype=float)
lat3=np.array(lat3, dtype=float)
u3=np.array(u3, dtype=float)
u3[u3==9999]=np.nan

a = pd.read_csv('0913am/0913am.TcoN',skiprows=39)
A = a.to_numpy()
v3=A[:,7]
v3=np.array(v3, dtype=float)
v3[v3==9999]=np.nan

a = pd.read_csv('0913am/0913am.TcoV',skiprows=39)
A = a.to_numpy()
Us3=A[:,7]
Us3=np.array(Us3, dtype=float)
Us3[Us3==9999]=np.nan

a = pd.read_csv('0913pm/0913pm.TcoE',skiprows=39)
A = a.to_numpy()
lon4=A[:,4]
lat4=A[:,3]
u4=A[:,7]
lon4=np.array(lon4, dtype=float)
lat4=np.array(lat4, dtype=float)
u4=np.array(u4, dtype=float)
u4[u4==9999]=np.nan

a = pd.read_csv('0913pm/0913pm.TcoN',skiprows=39)
A = a.to_numpy()
v4=A[:,7]
v4=np.array(v4, dtype=float)
v4[v4==9999]=np.nan

a = pd.read_csv('0913pm/0913pm.TcoV',skiprows=39)
A = a.to_numpy()
Us4=A[:,7]
Us4=np.array(Us4, dtype=float)
Us4[Us==9999]=np.nan

umax=40
uA=u*np.nan
vA=v*np.nan
u2A=u2*np.nan
v2A=v2*np.nan
u3A=u3*np.nan
v3A=v3*np.nan
u4A=u4*np.nan
v4A=v4*np.nan

for i in range(0, 47, 1):
    if Us[i] > umax:
        uA[i] = u[i]*umax/Us[i]
        vA[i] = v[i]*umax/Us[i]
        u[i] = np.nan
        v[i] = np.nan

for i in range(0, 125, 1):
    if Us2[i] > umax:
        u2A[i] = u2[i]*umax/Us2[i]
        v2A[i] = v2[i]*umax/Us2[i]
        u2[i] = np.nan
        v2[i] = np.nan

for i in range(0, 91, 1):
    if Us3[i] > umax:
        u3A[i] = u3[i]*umax/Us3[i]
        v3A[i] = v3[i]*umax/Us3[i]
        u3[i] = np.nan
        v3[i] = np.nan

for i in range(0, 47, 1):
    if Us4[i] > umax:
        u4A[i] = u4[i]*umax/Us4[i]
        v4A[i] = v4[i]*umax/Us4[i]
        u4[i] = np.nan
        v4[i] = np.nan


blevels = np.arange(-30,2.,2.)
N = len(blevels)-1
cmap2 = custom_div_cmap(N, mincol='DarkBlue', midcol='CornflowerBlue' ,maxcol='w')
cmap2.set_over('0.7') # set positive values (land) as light gray

fig,ax=plt.subplots(figsize=(10,4))
Q=plt.quiver(lon[0:-1:3],lat[0:-1:3],u[0:-1:3],v[0:-1:3],scale=300,width=0.005)
plt.quiver(lon3[0:-1:3],lat3[0:-1:3],u3[0:-1:3],v3[0:-1:3],scale=300,width=0.005)
plt.quiver(lon[0:-1:3],lat[0:-1:3],uA[0:-1:3],vA[0:-1:3],scale=300,color='r',width=0.005)
plt.quiver(lon3[0:-1:3],lat3[0:-1:3],u3A[0:-1:3],v3A[0:-1:3],scale=300,color='r',width=0.005)
ax.quiverkey(Q, 0.3, 0.8, 40, r'$40 \frac{cm}{s}$', labelpos='E',
                   coordinates='figure')

fig,ax=plt.subplots(figsize=(10,4))
Q=plt.quiver(lon2[0:-1:3],lat2[0:-1:3],u2[0:-1:3],v2[0:-1:3],scale=300,width=0.005)
plt.quiver(lon4[0:-1:3],lat4[0:-1:3],u4[0:-1:3],v4[0:-1:3],scale=300,width=0.005)
plt.quiver(lon2[0:-1:3],lat2[0:-1:3],u2A[0:-1:3],v2A[0:-1:3],scale=300,color='r',width=0.005)
plt.quiver(lon4[0:-1:3],lat4[0:-1:3],u4A[0:-1:3],v4A[0:-1:3],scale=300,color='r',width=0.005)
ax.quiverkey(Q, 0.3, 0.8, 40, r'$40 \frac{cm}{s}$', labelpos='E',
                   coordinates='figure')
