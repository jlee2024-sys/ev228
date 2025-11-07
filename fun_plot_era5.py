import matplotlib.pyplot as plt

def map(in_da, title='', cblabel='', out_path='', out_name=''):
    ''' This function plots a map from a 2D DataArray.
     
      Arguments:
      in_da -- the data array to be mapped.
      title -- the title of the graph.
      cblabel -- the label (units) for the colorbar.
      out_path -- the path on to where the image is saved on the device.
      out_name -- the name the image is saved under on the device.

      Outputs:
      None; saves an image to the device but doesn't return a value.
      '''
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