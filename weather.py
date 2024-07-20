import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

from datetime import datetime
import pytz

def get_forecast(user_ip: str = 'cache', lat: float = 52.52, lon: float = 13.41):

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('cache/' + user_ip, expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    #print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    #print(f"Elevation {response.Elevation()} m asl")
    #print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    #print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data = hourly_data)

    utc = pytz.UTC
    current_dateTime = datetime.now()
    ind = 0
    times = []
    temperatures = []
    #print(utc.localize( current_dateTime ))
    #print(hourly_dataframe['date'][12])
    #print( hourly_dataframe['date'][0] > utc.localize( current_dateTime ))
    for i in range(len(hourly_dataframe)):
        if hourly_dataframe['date'][i] >= utc.localize( current_dateTime ):
            times.append( int( hourly_dataframe['date'][i].time().hour ) )
            temperatures.append( round( float( hourly_dataframe['temperature_2m'][i] ) ) )
    d = {'times': times, 'temperatures': temperatures}
    #print(d)
    return d

#get_forecast()