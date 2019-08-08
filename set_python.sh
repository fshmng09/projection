#!/bin/bash
pip install --upgrade pip
pip install numpy
pip install scipy
pip install matplotlib
pip install Pillow
pip install ipython[all]
pip install pandas
#pip install seaborn
pip install jupyter


#pip install scikit-learn
#pip install tensorflow
#pip install keras


#sudo pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz

pip install geos
pip install proj
pip install netCDF4
pip install pyresample

#brew install geos
pip3 install https://github.com/matplotlib/basemap/archive/master.zip


#set gdal
brew unlink gdal
brew tap osgeo/osgeo4mac && brew tap --repair
brew install jasper netcd jpeg-turbo hdf4 osgeo/osgeo4mac/osgeo-libkml SFCGAL armadillo cryptopp
brew install gdal2 --with-armadillo --ignore-deoendencies
brew link --force gdal2
pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
