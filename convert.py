#coding:utf-8
import os
import glob

def nc2gtiff(input_name, epsg_in=3413, epsg_out=3857):
    """
    Convert file format from netCDF to geotiff.
    At first, change file format from netCDF to geotiff.
    In the first stage, epsg code is not changed.
    Second, change epsg code of geotiff file.

    You can select subdataset name to convert by defining sub_name.


    Parameters
    -----
    @input
    input_name:str: "./data/nc/hoge.nc"
    epsg_in:int: epsg code of input file
    epsg_out:int:epsg code of output file you want to make 

    @output
    Nan

    @outfile
    ./data/tiff/hoge_dX.geotiff
    ./data/tiff/hoge_dY.geotiff
    ------
    reference
    - gdal:
    Library to translate rastar and vector geospatial data formats
    https://gdal.org/

    - gdalinfo: shell command to see subdataset name in netCDF 
    ex)gdalinfo hoge.nc

    - gdal_translate
    Converts raster data between different formats.
    https://gdal.org/programs/gdal_translate.html
    https://gdal.org/drivers/raster/netcdf.html

    - gdalwarp
    Image reprojection and warping utility
    https://gdal.org/programs/gdalwarp.html

    - projection
    Current projected coordinate system: https://epsg.io/3413
    Final coordinate system for GEE:  https://epsg.io/3857

    """
    sub_name=["dX","dY"]
    
    for sub in sub_name:

        #netCDF to geotiff (EPSG code is not changed) 
        out_name = "./data/tiff_raw/{}_{}_tmp.tiff".format(os.path.basename(input_name)[:-3],sub)
        #c is shell command
        c  = "gdal_translate -a_srs EPSG:{epsg} NETCDF:'{in_name}':{sub} -of \
        'Gtiff' '{out_name}'".format(epsg=epsg_in,sub=sub, \
                                in_name=input_name,out_name=out_name) 
        result = os.system(c) #run shell command
        #print(c) #if you want to see the filled c, remove '#' in the head of this line
        if result!=0: # if it raises error, return filename 
            print(input_name, result, "translate")
        
        #geotiff EPSG_in to EPCG_out
        target_name="./data/tiff_target/{}_{}.tiff".format(os.path.basename(input_name)[:-3],sub)
        c = "gdalwarp -overwrite  {out_name} \
            {target_name} -s_srs EPSG:{epsg_in} -t_srs EPSG:{epsg_out} -of \
                'GTIFF'".format(out_name=out_name, target_name=target_name, 
                            epsg_in=epsg_in, epsg_out=epsg_out)
        result = os.system(c) # run shell command
        if result!=0:
            print(input_name, result, "warp")



if __name__=="__main__":
    filelist = glob.glob("./data/nc/*.nc")
    for input_name  in filelist:
        print(input_name)
        nc2gtiff(input_name)

    