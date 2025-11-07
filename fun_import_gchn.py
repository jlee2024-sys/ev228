import pandas as pd

def import_ghcn(file_path='', var=''):
    ''' Import GHCN weather station data.
    
    Arguments:
    file_path -- the path where the file is saved on the device (this includes the file name!)
    var -- the variable of interest in the dataset that we wish to return.

    Outputs:
    df_data -- A 1D dataframe of the data for the variable of interest.
    df_yr -- A 1D dataframe of the years from the dataset.
    
    '''
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_yr = df['YEAR']

    return df_data, df_yr