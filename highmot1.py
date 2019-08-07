import scipy as sp # scientific Python
import numpy.ma as ma # handling of masked arrays
import numpy as np 
from netCDF4 import Dataset # reading of netCDF files
from matplotlib.pyplot import title,figure,show,savefig,colorbar
from mpl_toolkits.basemap import Basemap # a map projection tool
from matplotlib import cm                         # colormap
import matplotlib.pyplot as plt
import os
from pathlib import Path
import glob

value=15
tot=0
drift=np.zeros((177, 119))
freq=np.zeros((177, 119))
my_dirs = "/Users/mariapinavomero/Documents/nh_drift/2019/spring19/data/*"
directory = glob.glob(my_dirs)
print(directory)

for file in directory:
    filename = file
    print(filename)
    #filename = os.fsdecode(file)
    if filename.endswith(".nc"): #or filename.endswith(".py"):  
        file=Dataset(filename, 'r', format='NETCDF3')
    #The displacement vectors are stored as origin and destination points of
    #each detected displacement and are selected from the file object:
    #lon0=sp.array(file.variables['lon'], dtype=float)
    #lat0=sp.array(file.variables['lat'], dtype=float)
        lon0 = file.variables['lon'][:]
        lat0 = file.variables['lat'][:]
        fv = file.variables['lon1']._FillValue
        lon1 = ma.array(file.variables['lon1'][0,:],dtype=float,fill_value=fv)
        lat1 = ma.array(file.variables['lat1'][0,:],dtype=float,fill_value=fv)
    #Note that the destination points lon1 and lat1 are provided as masked
    # arrays, taking missing data into account. The missing data masks need to
    # be set:
        lon1.mask=lon1.data==lon1.fill_value
        lat1.mask=lat1.data==lat1.fill_value
    #The calculation of the displacement vectors cannot be done in the lat/lon
    # domain but must be done in cartesian koordinates. Therefore, a coordinate
    # system must be defined. The same map projection is choosed as in which
    # the gridded AMSR-E data is available. To define such a map
    # projection, the matplotlib tool Basemap is used:
        Dmap = Basemap(projection='npstere',lon_0=315.,boundinglat=69,\
                       lat_ts=70, resolution='l',rsphere=(6378273.,6356889.))
    #The origin and destination points of each displacement vector can now
    # easily be computed in the native map projection grid. Difference yields
    # the displacement vectors:
        x0,y0 = Dmap(lon0,lat0)
        x1,y1 = Dmap(lon1,lat1)
        x_l=x0 - 0.5*62.5*1000
        y_l=y0 + 0.5*62.5*1000
        u = x1-x0
        v = y1-y0
        l_km=pow((pow(u,2) + pow(v,2)),0.5) / 1000
        lmax=l_km.max()
#create daily frequency map
        daily=l_km
        daily[daily>lmax]=0
        daily[daily<value]=0
        daily[daily>=value]=1

#sum
        drift=drift+l_km
        freq=freq+daily
        tot=tot+1

drift=drift/tot
drift[drift<value]=0

root_grp = Dataset('/Users/mariapinavomero/Documents/nh_drift/2019/spring19/data/nc/example.nc',
                   'w')#,
                   #format='NETCDF3')
#nv = rootgrp.createDimension("nv", 2)
time = root_grp.createDimension("time", 1)
xc = root_grp.createDimension("xc", 119)
yc = root_grp.createDimension("yc", 177)
time = root_grp.createVariable("time","f4",("time",))
xc = root_grp.createVariable("xc","f4",("xc",))
yc = root_grp.createVariable("yp","f4",("yc",))
frequency = root_grp.createVariable("frequency","f4",("time","yc","xc",))
highdrift = root_grp.createVariable("highdrift","f4",("time","yc","xc",))
#frequency = roo_tgrp.createVariable("frequency","f4",("yc","xc",))
#highdrift = root_grp.createVariable("highdrift","f4",("yc","xc",))
frequency[:]=freq
highdrift[:]=drift
root_grp.close()






    

