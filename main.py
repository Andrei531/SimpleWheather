import requests
import json

#GET A CITY DATA
#  city
class WeatherClient:
    def __init__ (self,city):

        position_url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": f"{city}"}

        response = requests.get(position_url, params=params)
        data = response.json()

        obj_city = data["results"][0]
        self.latitude = obj_city['latitude']
        self.longitude = obj_city['longitude']
        self.timezone = obj_city['timezone']

    #get weather data
    def get_weather(self):
        forecast_url = "https://api.open-meteo.com/v1/forecast"
        params = {"latitude": self.latitude,
                  "longitude": self.longitude,
                  "daily": ["temperature_2m_max", "temperature_2m_mean", "temperature_2m_min"],
                  "hourly": ["wind_speed_10m","temperature_2m"],
                  "forecast_days":1,
                  "timezone": self.timezone}
        response = requests.get(forecast_url, params=params)
        data = response.json()
        return data

    # get temperature
    def get_temperature(self,data):
        temp  = data ["hourly"]["temperature_2m"]
        return temp

    # get wind speed
    def get_wind_speed(self,data):
        wind_speed = data["hourly"]["wind_speed_10m"]
        return wind_speed

    # get tomorrow forecast
    def get_summary(self,temp,wind,data):
        time = data["hourly"]["time"]
        print(f" TIME | TEMP | WIND")
        for tm,tt,tw in zip(time,temp,wind):

            print (f"{tm[-5:]:5} | {tt:4} | {tw:4}" )





#MAIN
#city = input(str())
city_name = "Warsaw"
city = WeatherClient(city_name)
city_data = city.get_weather()

wind = city.get_wind_speed(city_data)
temp = city.get_temperature(city_data)
city.get_summary(temp,wind,city_data)





#WHEATHER FORECAST









