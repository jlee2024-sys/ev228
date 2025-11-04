import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def import_ghcn(file_path='', var=''):
    ''' Import GHCN weather station data '''
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_yr = df['YEAR']

    return df_data, df_yr

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('years')
    plt.xlim(1892, 2025)
    plt.ylabel('annual temperature (deg C)')
    plt.title('SGM00061600 St Louis, Senegal 1892-2025')
    #plt.show()
    plt.savefig(out_path + out_name, dpi=400)

fp = '/Users/julienlee/Documents/ev228_data/'
fn = 'SGM00061600_temp_189201-202508.csv'
fig_path = '/Users/julienlee/Documents/plots/'
fig_name = 'sgm_1.png'

var = 'metANN'
time_var = 'YEAR'

df, df_year = import_ghcn(file_path = fp + fn, var=var)

filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

mean = np.mean(filter_data)
stdev = np.std(filter_data)
max = np.max(filter_data)
min = np.min(filter_data)

print(mean, stdev, max, min)

timeseries(filter_data, in_x=filter_year, out_path = fig_path, out_name=fig_name)