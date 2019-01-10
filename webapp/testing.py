import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from bokeh.embed import components
from bokeh.plotting import figure, output_file, show


def message():
    import random
    index = random.randint(1,10000)

    #Load and prepare the the data
    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')
    data = pd.concat([weather_data, bus_data], axis=1, sort=False)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], infer_datetime_format=True)

    weather = data['Icon'][index]

    var1= ['cloudy','fog', 'snow', 'partly-cloudy-night' ,'clear-night', 'clear-day',
     'partly-cloudy-day', 'non']
    var2 = [0.00012011269365254887, 0.0012231992010086142, 0.012379481043480479, 7.412790384903038e-07, 4.856344616839285e-05,
     1.0, 0.06987925663016215, 0.798908506345788]
    var3 = [1.4, 1.8, 1.5, 1.4, 1.4,
     1.6, 1.5, 1.5]

    i = var1.index(weather)
    status = var3[i]

    post = "Hello! The weather today is %s, in this weather buses are typically %f miles away" % (weather, status)

    return post

print message()
def scatter_plots():

    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')

    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    # prepare some data
    list1 = list(data["Stops away"][1:10079])
    list2 = list(data["Distance"][1:10079])

    p = figure(plot_width=800, plot_height=400)

    # add a circle renderer with a size, color, and alpha

    print list(data["Stops away"][1:10079])

    #p.circle(list(data["Stops away"][1:10079]), list(data["Distance"][1:10079]), size=2, color="navy", alpha=0.5)

    p.circle(list1, list2, size=2, color="navy", alpha=0.5)

    # show the results

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels


    # show the results
    show(p)

    return p




def plots():

    from bokeh.plotting import figure, output_file, show

    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')

    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    # prepare some data
    x = data["Stops away"][1:10079]
    y = data["Distance"][1:10079]

    print x

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    # show the results
    show(p)

    return p

def plot_hist():

    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')

    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    ax = data.plot(x='Timestamp', y='Distance')

    fig = ax.get_figure()
    response = fig.savefig('hist.png')

    return response