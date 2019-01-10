from bokeh.io import show, output_file
from bokeh.plotting import figure

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from bokeh.embed import components
from bokeh.plotting import figure, output_file, show

from bokeh.palettes import Spectral6

output_file("bars.html")

bus_data = pd.read_csv('SIOT-data-bus.csv')
weather_data = pd.read_csv('SIOT-data-weather.csv')

data = pd.concat([weather_data, bus_data], axis=1, sort=False)

values = data['Icon'].value_counts()
print values[0]

print values

fruits = ['Snow', 'Cloudy', 'Clear night', 'Partly Cloudy Night', 'Clear day', 'Partly Cloudy Day', 'Fog']
counts = data['Icon'].value_counts()

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9, color='gray')


p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)