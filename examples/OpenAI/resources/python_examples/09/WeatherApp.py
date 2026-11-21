# Fig. 9.2: WeatherApp.py
"""Use an OpenWeather web service to get a city's current weather."""
import os
import requests
import sys

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def get_weather(city, api_key):
    """Get current weather data for city from OpenWeather."""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': api_key}
    
    # invoke the web service using the requests module
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status() # raise exception if HTTP error occurs

    return response.json() # converts JSON response to a Python dictionary

def display_weather(weather_data):
    """Display selected weather data from OpenWeather response."""
    weather = weather_data['weather'][0]
    main_data = weather_data['main']

    # convert temps to Fahrenheit
    current_f_temp = celsius_to_fahrenheit(main_data['temp'])
    feels_like_f_temp = celsius_to_fahrenheit(main_data['feels_like'])

    # generate the icon URL
    icon = weather['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon}@4x.png'

    print(f'{weather_data["name"]} Weather')
    print(f'Temperature: {main_data["temp"]:.1f} C',
        f'({current_f_temp:.1f} F)')
    print(f'Feels like: {main_data["feels_like"]:.1f} C',
        f'({feels_like_f_temp:.1f} F)')
    print(f'Humidity: {main_data["humidity"]}%')
    print(f'Conditions: {weather["description"]}')
    print(f'Icon: {icon_url}')

def main():
    """Get and display current weather for a city."""
    if len(sys.argv) != 2:
        print(f'Usage: ipython {sys.argv[0]} <city>')
        sys.exit(1)

    # get API key and confirm it exists
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if api_key is None or api_key.strip() == '':
        print('OPENWEATHER_API_KEY environment variable is not set.')
        sys.exit(1)

    # get and display weather report for specified city
    try:
        display_weather(get_weather(sys.argv[1], api_key))
    except requests.HTTPError as error:
        print(f'Terminating due to HTTPError:\n{error}')
    except requests.RequestException as error:
        print(f'Terminating due to RequestException: {error}')

# check whether this file was executed as a script and, if so, call main
if __name__ == '__main__': 
    main()




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
