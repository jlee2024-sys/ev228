import matplotlib.pyplot as plt

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe
       
       Arguments:
       in_df -- 1D dataframe with data to be plotted (y-axis).
       in_x -- dataframe of x-axis to be plotted.
       out_path -- the path on to where the image is saved on the device.
       out_name -- the name the image is saved under on the device.

       Outputs:
       None; saves an image to the device but doesn't return a value.
       '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('Years')
    plt.xlim(1948, 2025)
    plt.ylabel('Annual Temperature (deg C)')
    plt.title('ASM00094998 Macquarie Island, Australia 1948-2025')
    #plt.show()
    plt.savefig(out_path + out_name, dpi=400)