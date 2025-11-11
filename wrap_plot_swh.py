import sys
import numpy as np
import scipy.stats as stats
import fun_import_era5 as imp
import fun_plot_era5 as plotter

#All datasets are netCDFs from ERA5's database.
filepath = '/Users/julienlee/Documents/ev228_data/'
wave_fn = 'era5_wave_height_1960-2025.nc'
temp_fn = 'era5_ocean_surface_temp_1960-2025.nc'
wind_fn = 'era5_wind_speed_1960-2025.nc'

#Import data.
da_swh, yrs = imp.import_era5(filepath + wave_fn, 'swh')
da_sst, yrs = imp.import_era5(filepath + temp_fn, 'sst')
da_10mws, yrs = imp.import_era5(filepath + wind_fn, 'si10')

#Set target location.
target_lat = 37.5
target_lon = 237.0

#Dimensional reduction.
#Get a single latitude, then eliminate extra dimensions with .mean(). Then do the same for longitude.
da_swh_target_lat = da_swh.where(da_swh['latitude'] == target_lat, drop = True)
da_swh_target_lat = da_swh_target_lat.mean('latitude')
da_swh_target_latlon = da_swh_target_lat.where(da_swh_target_lat['longitude'] == target_lon, drop = True)
da_swh_target_latlon = da_swh_target_latlon.mean('longitude')

#Line graph of swh vs time at target location.
plotter.graph(yrs, da_swh_target_latlon, xlab='Years', ylab='swh (m)', title=
            'Significant Wave Height at ('+ str(target_lat) + ', ' + str(target_lon) + '), 1960-2025', 
            out_path='/Users/julienlee/Documents/plots/', out_name='wave_vs_yrs.png')

#Get linear regression statistics.
slope, y_int, r_val, p_val, std_err = stats.linregress(np.arange(0, 790), da_swh_target_latlon.data)

#Scatter plot of swh vs time at target location with linear regression line.
plotter.regress_graph(yrs.dt.year, da_swh_target_latlon, y_int, slope, xlab='Years', ylab='swh (m)', title=
                    'Significant Wave Height at ('+ str(target_lat)+', '+str(target_lon)+'), 1960-2025',
                    out_path='/Users/julienlee/Documents/plots/', out_name='wave_vs_yrs_2.png')

#Dimensional reduction.
#Average out the time variable.
da_swhtimemn = da_swh.mean('valid_time')
da_ssttimemn = da_sst.mean('valid_time') - 273.15
da_10mwstimemn = da_10mws.mean('valid_time')

#Maps of significant wave height, surface temperature, and wind speeds.
plotter.map(da_swhtimemn, title='ERA5 Mean Significant Wave Height (swh), 1940-2025',
           cblabel='meters', out_path='/Users/julienlee/Documents/plots/', out_name='wave_plot.png')
plotter.map(da_ssttimemn, title='ERA5 Mean Surface Temperature (°C), 1960-2025',
           cblabel='°C', out_path='/Users/julienlee/Documents/plots/', out_name='temp_plot.png')
plotter.map(da_10mwstimemn, title='ERA5 10m Wind Speed (m/s), 1960-2025',
           cblabel='m/s', out_path='/Users/julienlee/Documents/plots/', out_name='wind_plot.png')

sys.exit('stop')

#Attempt to calculate the average of the slopes of the regression lines across spacial points.
#Currently doesn't throw an error but doesn't finish running either.
slope_sum = 0
point_sum = 0
for lon in range(0, 359):
    for lat in range(-90, 90):
        da_swh_target_lat = da_swh.where(da_swh['latitude'] == lat, drop = True)
        da_swh_target_lat = da_swh_target_lat.mean('latitude')
        da_swh_target_latlon = da_swh_target_lat.where(da_swh_target_lat['longitude'] == lon, drop = True)
        da_swh_target_latlon = da_swh_target_latlon.mean('longitude')
        regress = stats.linregress(np.arange(0, 790), da_swh_target_latlon.data)
        slope_sum += regress.slope
        point_sum += 1

avg_slope = slope_sum/point_sum
print(str(avg_slope)+': average swh increase (m/mo)')