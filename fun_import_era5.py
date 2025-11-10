import xarray as xr
import pandas as pd

def import_era5(file_path='', var=''):
    ''' This function imports ERA5 gridded data and returns the data for a specific variable.
    
    Arguments:
    file_path -- the path where the file is saved on the device (this includes the file name!)
    var -- the variable of interest in the dataset that we wish to return.
    
    Outputs:
    da -- the DataArray of the data from the variable of interest.
    (yr)
    '''
    ds = xr.open_dataset(file_path)
    da = ds[var]
    yr = ds['valid_time']

    return da, yr

def import_as_csv(filepath='', outpath='', var=''):
    ds = xr.open_dataset(filepath)
    ds.to_dataframe().to_csv(outpath)
    df = pd.read_csv(outpath)
    df_data = df[var]
    df_yr = df['valid_time']

    return df_data, df_yr