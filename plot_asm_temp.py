import numpy as np
import fun_import_gchn as imp
import fun_plot_timeseries as pt

fp = '/Users/julienlee/Documents/ev228_data/'
fn = 'ASM00094998_temp_194804-202508.csv'
fig_path = '/Users/julienlee/Documents/plots/'
fig_name = 'asm_temp.png'

var = 'metANN'
time_var = 'YEAR'

#stores annaul temp and years from Macquarie Island data
df, df_year = imp.import_ghcn(file_path = fp + fn, var=var)

#years of apparently outlying temperature
print(df_year[df < 3.9])
print(df_year[df == 5.95])

#filters out 999.9 data points
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

#calculates, prints descriptive statistics
mean = np.mean(filter_data)
stdev = np.std(filter_data)
max = np.max(filter_data)
min = np.min(filter_data)

print(mean, stdev, max, min)

#saves timeseries graph of annual temp over time at Macquarie Island
pt.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)
