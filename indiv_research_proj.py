import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import fun_import_era5 as imp
import fun_plot_era5 as mapper

def open_var_timemn(fp, fn, var):
    ds = xr.open_dataset(fp + fn)
    da_var = ds[var]
    da_timemn = da_var.mean('valid_time')

filepath = '/Users/julienlee/Documents/ev228_data/'
wave_fn = 'era5_wave_data_1940-2025.nc'
temp_fn = 'era5_ocean_surface_temp_1960-2025.nc'


da_swh = imp.import_era5(filepath + wave_fn, 'swh')
da_temp = imp.import_era5(filepath + temp_fn, 'sst')


da_swhtimemn = da_swh.mean('valid_time')
da_ssttimemn = da_temp.mean('valid_time') - 273.15

mapper.map(da_swhtimemn, title='ERA5 Mean Significant Wave Height (swh), 1940-2025',
           cblabel='meters', out_path='/Users/julienlee/Documents/plots/', out_name='wave_plot.png')
mapper.map(da_ssttimemn, title='ERA5 Mean Surface Temperature (deg C), 1960-2025',
           cblabel='deg C', out_path='/Users/julienlee/Documents/plots/', out_name='temp_plot.png')

'''

da_timemn.plot()
plt.show()

#map = plt.pcolormesh(da_timemn['longitude'], da_timemn['latitude'], da_swh)
#cb = plt.colorbar(map)
#cb.set_label("meters")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title("Average Significant Wave Height (swh), 1940-2025")
plt.show()

make a plot for surface temperature data. 
Make the plots look nice.
compare the plots.
Potenitally also make a plot for wind data

Potentially add a time component to plots.
Potentially add statistics describing correlation levels.


'''