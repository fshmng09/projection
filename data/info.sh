gdalinfo ./nc/ice_drift_nh_polstere-625_multi-oi_201902271200-201903011200.nc >>raw.txt
gdalinfo NETCDF:"./nc/ice_drift_nh_polstere-625_multi-oi_201902271200-201903011200.nc":dX >> sub.txt
gdalinfo ./tiff_raw/ice_drift_nh_polstere-625_multi-oi_201902271200-201903011200_dX_tmp.tiff >>tiffraw.txt
gdalinfo ./tiff_target/ice_drift_nh_polstere-625_multi-oi_201902271200-201903011200_dX.tiff >>target.txt
open sub.txt
open raw.txt
open tiffraw.txt
open target.txt
