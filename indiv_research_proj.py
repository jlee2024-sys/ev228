import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr

filepath = '/Users/julienlee/Documents/ev228_data/'
filename = 'era5_wave_data_1940-2025.nc'

ds = xr.open_dataset(filepath + filename)
#print(ds)

da_swh = ds['swh']
#print(da_swh)

da_timemn = da_swh.mean('valid_time')

da_timemn.plot()
plt.show()
