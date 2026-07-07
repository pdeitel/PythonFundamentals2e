# Fig. 9.2: WeatherApp.py
"""Use an OpenWeather web service to get a city's current weather."""
import os
import requests


def get_weather(city, api_key):
    """Get current weather data for city from OpenWeather."""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': api_key}

    # invoke the web service using the requests module
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # raise exception if HTTP error occurs

    return response.json()  # converts JSON to dictionaries & lists


def display_weather(city, weather_data):
    """Display selected weather data from OpenWeather response."""
    weather = weather_data['weather'][0]
    main = weather_data['main']

    # converts celsius to Fahrenheit
    f_temp = main['temp'] * 9 / 5 + 32
    feels_like_f_temp = main['feels_like'] * 9 / 5 + 32

    # generate the icon URL
    icon = weather['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon}@4x.png'

    print(f'{city} Weather')
    print(f'Temperature: {main["temp"]:.1f} C ({f_temp:.1f} F)')
    print(f'Feels like: {main["feels_like"]:.1f} C',
        f'({feels_like_f_temp:.1f} F)')
    print(f'Humidity: {main["humidity"]}%')
    print(f'Conditions: {weather["description"]}')
    print(f'Icon: {icon_url}')


# get and display weather report for specified city
city = input('Enter a city (e.g., Houston,TX,USA): ')
weather_data = get_weather(city, os.getenv('OPENWEATHER_API_KEY'))
display_weather(city, weather_data)

##########################################################################
# (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
