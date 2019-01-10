from flask import Flask, render_template, request
from flask import Flask, make_response
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show

app = Flask(__name__)


@app.route("/")
def home():
    #Prepare data for plotting
    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')
    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    # Create scatter plot
    stops = "Stops away"
    distance = "Distance"
    scatplot_1 = scatter_plots(data, stops, distance)
    # Embed plot into HTML via Flask Render
    script, div = components(scatplot_1)

    #Create scatter plot 2
    distance = "Distance"
    temperature = "Temperature"

    scatplot_2 = scatter_plots(data, distance, temperature)
    script2, div2 = components(scatplot_2)

    #Create snow histogram
    histogram_1 = histogram()
    script3, div3 = components(histogram_1)


    return render_template('index.html', script = script,
    div = div, script2 = script2, div2 = div2, script3 = script3, div3 = div3)

def histogram():

    #output_file("bars.html")
    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')

    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    #values = data['Icon'].value_counts()
    fruits = ['Snow', 'Cloudy', 'Clear night', 'Partly Cloudy Night', 'Clear day', 'Partly Cloudy Day', 'Fog']
    counts = data['Icon'].value_counts()

    p = figure(x_range=fruits, plot_height=250, title="Weather Icon Counts",
               toolbar_location=None, tools="")

    p.vbar(x=fruits, top=counts, width=0.9)

    p.yaxis.axis_label = "Counts"

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    #show(p)
    return p

def scatter_plots(data, var1, var2):

    list1 = list(data[var1][1:10079])
    list2 = list(data[var2][1:10079])

    #initiate figure
    p = figure(plot_width=800, plot_height=400)

    # Create scatter plot
    p.circle(list1, list2, size=2, color="navy", alpha=0.5)

    p.xaxis.axis_label = var1
    p.yaxis.axis_label = var2
    # output to static HTML file
    output_file("lines.html")

    # show the results: for debugging
    #show(p)

    return p


def create_figure():

    # output to static HTML file
    #output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

    # show the results
    return p


@app.route("/forward", methods=['GET', 'POST'])
def forward():

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

    post = "Hello! The weather today is %s, in this weather buses are typically %f miles away." % (weather, status)

    post = post
    #return render_template("message.html", post = post)

    #Prepare all graphs

    #Prepare data for plotting
    bus_data = pd.read_csv('SIOT-data-bus.csv')
    weather_data = pd.read_csv('SIOT-data-weather.csv')
    data = pd.concat([weather_data, bus_data], axis=1, sort=False)

    # Create scatter plot
    stops = "Stops away"
    distance = "Distance"
    scatplot_1 = scatter_plots(data, stops, distance)
    # Embed plot into HTML via Flask Render
    script, div = components(scatplot_1)

    #Create scatter plot 2
    distance = "Distance"
    temperature ="Temperature"

    scatplot_2 = scatter_plots(data, distance, temperature)
    script2, div2 = components(scatplot_2)

    #Create snow histogram
    histogram_1 = histogram()
    script3, div3 = components(histogram_1)

    return render_template('index.html', script=script,
                           div=div, script2=script2, div2=div2, script3=script3, div3=div3 , post = post)

if __name__ == "__main__":
    # plot_hist()
    app.run(debug=True)