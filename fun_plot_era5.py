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
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(title)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label(cblabel)
    plt.savefig(out_path + out_name)

def graph(x, y, xlab='', ylab='', title='', out_path='', out_name=''):
    ''' This function plots a generic graph (a line graph for this data) given two variables.
     
      Arguments:
      x -- the independent variable.
      y -- the dependent variable.
      xlab -- the label for the x-axis.
      ylab -- the label for the y-axis.
      title -- the title of the graph.
      out_path -- the path on to where the image is saved on the device.
      out_name -- the name the image is saved under on the device.

      Outputs:
      None; saves an image to the device but doesn't return a value.
      '''
    plt.plot(x, y, c="#004cce")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.savefig(out_path + out_name)

def regress_graph(x, y, y_int, slope, xlab='', ylab='', title='', out_path='', out_name=''):
    ''' This function plots a generic graph (a line graph for this data) given two variables.
     
      Arguments:
      x -- the independent variable.
      y -- the dependent variable.
      y_int -- the y-intercept of the regression line.
      slope -- the slope of the regression line.
      xlab -- the label for the x-axis.
      ylab -- the label for the y-axis.
      title -- the title of the graph.
      out_path -- the path on to where the image is saved on the device.
      out_name -- the name the image is saved under on the device.

      Outputs:
      None; saves an image to the device but doesn't return a value.
      '''
    plt.scatter(x, y)
    plt.plot(x, y_int+slope*x, 'r')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.savefig(out_path + out_name)
