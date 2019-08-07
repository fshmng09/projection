#!/usr/bin/python
import os
import sys
import glob
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.pylab import *
from osgeo import osr,gdal
from mpl_toolkits.basemap import Basemap
from matplotlib.pylab import *
from pyresample import kd_tree,geometry
from pyresample import load_area, save_quicklook, SwathDefinition
from netCDF4 import Dataset

filename='/Users/mariapinavomero/Documents/nh_drift/2018/0318/data/20180301.nc'

def plotBasemap(lons,lats,variable):
 
  # compute mean longitude,latitude
  # for center of Basemap plot
  lat0 = lons.mean()
  lon0 = lats.mean()
  #lon0 = <span class="skimlinks-unlinked">lons.mean</span>()
  #lat0 = <span class="skimlinks-unlinked">lats.mean</span>()
 
  # create basemap object in
  # polar-stereographic projection
  m = Basemap(projection='npstere',
  boundinglat=60.0,lon_0=300.0,resolution='h',area_thresh=50000)
  #lon_0=315.,boundinglat=69,\ lat_ts=70, resolution='l',rsphere=(6378273.,6356889.))
  m.drawcoastlines(linewidth=0.05)
 
  # add temperature data as scatter-plot on map
  x,y = m(lons,lats)
  m.scatter(x,y,c=variable,cmap=plt.cm.jet,edgecolors=None,s=0.15)
 
  # add plot title, colorbar
  plt.title('T')
  plt.colorbar()
 
  # save output to png
  plt.savefig('plottedPolarStereographic.png',dpi=500)
  plt.close()
 
def toGeotiff(regriddingResult,areaDef):
 
  # create GDAL driver for writing Geotiff
  driver = gdal.GetDriverByName('GTiff')
 
  # set nodata value of output array as 0.0
  outputImage = np.array(regriddingResult,dtype=np.float32)
  outputImage[outputImage==9999.0]=0.0
 
  # get output band dimensions
  nrows,ncols = regriddingResult.shape
 
  # create Geotiff destination dataset for output
  dstds = driver.Create('test.tif',ncols,nrows,1,gdal.GDT_Float32)
  gt = [ areaDef.area_extent[0],areaDef.pixel_size_x,0,\
  areaDef.area_extent[3],0,-areaDef.pixel_size_y]
 
  # seto geotransform of output geotiff
  dstds.SetGeoTransform(gt)
 
  # set-up projection of output Geotiff
  srs = osr.SpatialReference()
  srs.ImportFromProj4(areaDef.proj4_string)
  srs.SetProjCS(areaDef.proj_id)
  srs = srs.ExportToWkt()
  dstds.SetProjection(srs)
 
  # write array data (1 band) ... set NoData value at 0.0
  # in output Geotiff
  dstds.GetRasterBand(1).WriteArray(outputImage)
  dstds.GetRasterBand(1).SetNoDataValue(0.0)
  dstds=None
 
def main():
 
  # ----------------------------------------------
  # read 3 different float arrays from 3 a netcdf:
  #   (1) latitudes
  #   (2) longitudes
  #   (3) temperatures (degrees Kelvin)
  # ----------------------------------------------
 
  ncReader      = Dataset(filename,'r')
  temperatures  = ncReader['dX'][:]
  latitudes     = ncReader['lat'][:]
  longitudes    = ncReader['lon'][:]
  ncReader.close()
 
  # plot the X,Y,Z (Longitudes,Latitudes,Tempeatures)
  # using Python's basemap library
  plotBasemap( longitudes,latitudes,temperatures )
 
  # manually define Polar-stereographic projection
  # using a Python dictionary{}
 
  projection = 'stere'
  areaDict = dict(
    lat_0=90,
    lon_0=-45,
    k=1, x_0=0, y_0=0,
    a=6378273, b=6356889.449 ,
    proj=projection,units='m'
  )
 
  # define rectangular bounds for domain of output Geotiff
  areaExtent = (-3850000.0, -5350000.0, 3750000.0, 5850000.0)
 
  # names-strings for Pyresample regridding objects
  # (could be anything)
  areaID = 'nucaps swath data'
  areaName = 'nucaps granules'
 
  # create a Pyresample AreaDefinition() object
  # by passing-in output regridding dimensions (2000x2000),
  # projection object, area-bounds
 
  areaDef = geometry.AreaDefinition(
    areaID,
    areaName,
    projection,
    areaDict ,
    2000,
    2000,
    areaExtent
  )
 
  # create Pyresample SwathDefinition object, passing in
  # 1D NumPy arrays of longitudes and latitudes
  swathDef = geometry.SwathDefinition(lons=longitudes,lats=latitudes)
 
  # using Pyresample's resample_gauss() method to regrid satellite data
  # into polar stereographic projection
 
  regridding_result = kd_tree.resample_gauss(swathDef, temperatures.ravel(), \
  areaDef, radius_of_influence=70000, sigmas=25000)#fill_value=None)
 
  # write result to Geotiff
  toGeotiff(regridding_result,areaDef)
 
if __name__ == '__main__':
  main()
