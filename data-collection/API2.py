#!/usr/bin/python3

import json
from requests import get
from datetime import datetime


def get_weather_data():
    api_key = "161c02396c9dbad8b9a6a0997a4c866b"
    location = ("40.6795", "73.9992")  # Latitude and longitude for Carrol gardens, London

    Dark_data = "https://api.darksky.net/forecast/{}/{loc[0]:},{loc[1]:}?".format(api_key, loc=location)
    weather = get(Dark_data)
    currentW = json.loads(weather.text)['currently']  # Current weather data

    # Connvert UNIX time stamp to YMDHMS

    currentTime = currentW['time']
    timedate = datetime.fromtimestamp(int(currentTime)).strftime('%Y-%m-%d %H:%M:%S')

    return [timedate, currentW['cloudCover'], currentW['temperature'], currentW['humidity'],
            currentW['icon'], currentW['precipIntensity'], currentW['precipProbability']]

def process_data(raw_visit):
    FEET_PER_METER = 3.28084
    FEET_PER_MILE = 5280
    route = raw_visit['MonitoredVehicleJourney']['PublishedLineName']
    call = raw_visit['MonitoredVehicleJourney']['MonitoredCall']

    distances = call['Extensions']['Distances']
    monitored_stop = call['StopPointName']

    stops_away = distances['StopsFromCall']
    distance = round(distances['DistanceFromCall'] * FEET_PER_METER / FEET_PER_MILE, 2)

    return [route, monitored_stop, stops_away, distance]



def get_bus_data():
    STOP_MONITORING_ENDPOINT = "http://bustime.mta.info/api/siri/stop-monitoring.json"
    api_key = 'de1b81b8-4f7b-46f3-ad06-d6dac05c2d6c'
    line = 'B57'
    stop_id = 307910
    direction = 1
    max_visits = 1
    line_id = "MTA NYCT_%s" % line

    blob = {
        'key': api_key,
        'OperatorRef': "MTA",
        'MonitoringRef': stop_id,
        'LineRef': line_id,
        'MaximumStopVisits': max_visits,
    }

    payload = blob
    response = get(STOP_MONITORING_ENDPOINT, params=payload)

    rsp = response.json()

    parsed_visits = []
    visits_json = rsp['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']

    for raw_visit in visits_json:
        parsed_visits.append(process_data(raw_visit))

    return parsed_visits
