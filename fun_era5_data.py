import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr

def des_stats(path, name, dim1, dim2, dim3):
    ds = xr.open_dataset(path + name)
    dict_descrip = {
        'mean' : s
        'st_dev' : 
        'skewness' :
        'kurtosis' :
    }