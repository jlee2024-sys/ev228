import matplotlib.pyplot as plt

def map(in_da, title='', cblabel='', out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title(title)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label(cblabel)
    plt.savefig(out_path + out_name, dpi=400)