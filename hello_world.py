print('Sphinx of the black quartz, judge my vow')

import pandas as pd

filepath = '/Users/julienlee/Data/ev228/'
filename = 'KRDU_temp_188708-202508.csv'

df = pd.read_csv(filename)

print(df)