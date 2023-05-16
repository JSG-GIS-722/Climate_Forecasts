import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
from netCDF4 import *

ds_ini = xr.open_dataset("UK_WLHL.nc")
ds_renamed = ds_ini.rename({"water_limited_heat_stressed_potential_wheat_yield": "yields"})

# Use nas in t  as cookie cutter 
da_notnulls = ds_renamed.yields[0,:,:].notnull()
da_notnulls_bool = da_notnulls * 1

ds_land = ds_renamed.where(da_notnulls_bool == 1)

ds_land['time'] = pd.to_datetime(ds_land['time'], format = "%Y%m%d")

ds_resampled_time = ds_land.resample(time ='10Y').mean()
ds_resampled_loc = ds_land.resample(time ='10Y').mean(dim = ['x','y','time'])

ds_resampled_time.yields.isel(time=10).plot()
ds_resampled_loc.yields.plot()
