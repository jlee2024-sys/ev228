import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

def import_dataset_get_var (path, name, var_name):
    df = pd.read_csv(path + name)
    var_data = df[var_name]
    return var_data

lat = import_dataset_get_var ('/Users/julienlee/Documents/ev228_data/', 'NAS-eDNA-Download.csv', 'Latitude')
long = import_dataset_get_var ('/Users/julienlee/Documents/ev228_data/', 'NAS-eDNA-Download.csv', 'Longitude')
print(long)