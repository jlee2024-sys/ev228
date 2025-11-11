# ev228
Code for EV228 Block 3

Individual Research Project
Brief summary of project:
This project investigates the relationship between significant wave height, surface temperature, and wind speed in global oceans, as well as the change in significant wave height over time. The code saves global colormaps for the three variables and svaes line and regression graphs for significant wave height at a specified location over time.

Steps for important workflows:
First, I imported each of the three ERA5 datasets using the import_era5() function and got the key variable for each. To get swh data for a single location, I used .where() and .mean() to reduce the longitude and latitudes to set target values, and then used my plotter.graph() function to graph the swh data against time. The linear regression plot goes one step further, calculating the linear regression statistics with stats.linregress() and using them to overlay a regression line with a scatterplot of the data through my regress_graph() function. For maps, I averaged out the time variable and mapped them with the plotter.map() function.
Finally, I also attempt to print the average of the slopes of the regression lines across all spacial points. This would have allowed me to see how significant wave height was trending globally over the last 65 years. However, I haven't gotten it to output anything.

Index of code:
• fun_import_era5: contains the import_era5 function which imports the dataset and returns data arrays of a variable of interest and the time variable.
• fun_plot_era5: contains the functions map, which saves a colormap of imputted data; graph, which saves a line graph of the inputted data; and regress_graph, which saves a scatterplot of the inputted data with a regression line. 
• wrap_plot_swh: script calling the defined functions to create graphs with the desired inputs (file, target longitude and latitude, visual choices, etc.)

Generative AI statement:
I occasionally got code from Google's AI overview, although I didn't keep track of what specific code came from here. However, I found that getting code from old assignments or from the matplotlib, scipy and xarray documentation online was usually more helpful, so very little of the final code was sourced from generative AI.
