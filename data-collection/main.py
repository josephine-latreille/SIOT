#!/usr/bin/python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ~/SIOT2018/API2 import get_weather_data, get_bus_data, process_data

##### SENSING-IOT COURSEWORK 2018 #####

scope = scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sensing-iot-4164fbde31cc.json', scope)
client = gspread.authorize(creds)
sheet = client.open("SIOT-data")

try:
    weatherdata = get_weather_data()

    sheet.worksheet('weather').append_row(weatherdata)

    print('Weather data added')
except:

    print('No data found')

try:
    busdata = get_bus_data()

    sheet.worksheet('bus').append_row(busdata[0])
    print('Bus data added')

except:
    print('No data found')
