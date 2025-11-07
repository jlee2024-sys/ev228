import xarray as xr

def import_era5(file_path='', var=''):
    ''' This function imports ERA5 gridded data and returns the data for a specific variable.
    
    Arguments:
    file_path -- the path where the file is saved on the device (this includes the file name!)
    var -- the variable of interest in the dataset that we wish to return.
    
    Outputs:
    da -- the DataArray of the data from the variable of interest.'''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da