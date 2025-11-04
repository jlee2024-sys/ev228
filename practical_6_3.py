import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 si10 wind speed 1980-1989 mean')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('m/s')
    #plt.show()
    
    plt.savefig(out_path + out_name, dpi=400)

path = '/Users/julienlee/Documents/ev228_data/'
fn = 'era5_10mwind_1980-1989.nc'
out_path = '/Users/julienlee/Documents/plots/'
out_fn = '1_era5.png'

da = import_era5(file_path=path + fn, var='si10')
da_timemn = da.mean(dim='valid_time')

map(da_timemn, out_path=out_path, out_name=out_fn)