import sys
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import xarray as xr
import fun_import_era5 as imp
import fun_plot_era5 as mapper


filepath = '/Users/julienlee/Documents/ev228_data/'
wave_fn = 'era5_wave_height_1960-2025.nc'
temp_fn = 'era5_ocean_surface_temp_1960-2025.nc'
wind_fn = 'era5_wind_speed_1960-2025.nc'

#Not used right now.
ds = xr.open_dataset(filepath + wave_fn)

da_swh, yrs = imp.import_era5(filepath + wave_fn, 'swh')
da_sst, yrs = imp.import_era5(filepath + temp_fn, 'sst')
da_10mws, yrs = imp.import_era5(filepath + wind_fn, 'si10')

target_lat = 37.5
target_lon = 237.0


da_swhtimemn = da_swh.mean('valid_time')
da_ssttimemn = da_sst.mean('valid_time') - 273.15
da_10mwstimemn = da_10mws.mean('valid_time')


#Dimensional reduction.
#Get a single latitude, then eliminate extra dimensions with .mean(). Then do the same for longitude.
da_swh_target_lat = da_swh.where(da_swh['latitude'] == target_lat, drop = True)
da_swh_target_lat = da_swh_target_lat.mean('latitude')
da_swh_target_latlon = da_swh_target_lat.where(da_swh_target_lat['longitude'] == target_lon, drop = True)
da_swh_target_latlon = da_swh_target_latlon.mean('longitude')

#print(da_swh_target_latlon)


plt.plot(yrs, da_swh_target_latlon)
#plt.xlim(1960, 2025)
plt.xlabel('Years')
plt.ylabel('swh (m)')
plt.title('Significant Wave Height at ('+ str(target_lat) + ', ' + str(target_lon) + '), 1960-2025')
plt.show()

#Maps of significant wave height, surface temperature, and wind speeds. These work.
#mapper.map(da_swhtimemn, title='ERA5 Mean Significant Wave Height (swh), 1940-2025',
#           cblabel='meters', out_path='/Users/julienlee/Documents/plots/', out_name='wave_plot.png')
#mapper.map(da_ssttimemn, title='ERA5 Mean Surface Temperature (deg C), 1960-2025',
#           cblabel='deg C', out_path='/Users/julienlee/Documents/plots/', out_name='temp_plot.png')
#mapper.map(da_ssttimemn, title='ERA5 10m Wind Speed (m/s), 1960-2025',
#           cblabel='m/s', out_path='/Users/julienlee/Documents/plots/', out_name='wind_plot.png')

sys.exit('stop')

#These don't work:

#Attempt to get correlation coefficient
swh_arr=da_swhlonlatmn.to_numpy()
yrs_arr=yrs.to_numpy()
r = np.corrcoef(yrs_arr, swh_arr)
print(r)

#Attempt to import as a csv file
df_swh, df_yr = imp.import_as_csv(filepath+wave_fn, filepath+'era5_wave_height_1960-2025.csv', 'swh')
slope, y_int, r_val, p_val, std_err = stats.linregress(df_yr, df_swh)
print(slope, y_int, r_val, p_val, std_err)

print(da_swh['longitude'==0, 'latitude'==0])

target_lat = 0
target_lon = 0
point_data = da_swhtimemn['swh'].sel(lat=target_lat, lon=target_lon, method='nearest')
print(point_data)

stacked_data = ds.stack(paired_points=['latitude', 'longitude'])
def perform_linregress(group):
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            yrs.sel(paired_points=group.paired_points),
            group[da_swh]
        )
        return xr.DataArray([slope, intercept, r_value, p_value, std_err],
                            coords={'regression_stats': ['slope', 'intercept', 'r_value', 'p_value', 'std_err']})
regression_results = stacked_data.groupby('paired_points').apply(perform_linregress)




'''
Plan:

make a plot for surface temperature data. 
Make the plots look nice.
compare the plots.
Potenitally also make a plot for wind data

Potentially add a time component to plots.
Potentially add statistics describing correlation levels.


'''