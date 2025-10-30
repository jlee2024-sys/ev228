import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr

filepath = '/Users/julienlee/Documents/ev228_data/'
filename = 'era5_t2m_1997-2025.nc'

ds = xr.open_dataset(filepath + filename)
#print(ds)

da = ds['t2m']
#print(da)
da_timemn = da.mean('valid_time')

da_timemn.plot()
plt.show()
