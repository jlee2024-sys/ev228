
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

filepath = '/Users/julienlee/Documents/ev228_data/'
filename = 'KRDU_temp_188708-202508.csv'

df = pd.read_csv(filepath + filename)

print(df)