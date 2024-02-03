from configparser import ConfigParser
import argparse 
from configparser import ConfigParser
from urllib import parse

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_api_key():
    config = ConfigParser() 
    config.read('secrets.ini') 
    return config["openweathermap"]["api_key"] 

def read_user_cli_args():
    parser = argparse.ArgumentParser(description="Get weather and temperature for a city")
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()

def build_weather_query(city_input, imperial=False):

    """Builds the URL for an API request to OpenWeather's weather API.
    Args:
        city_input (List[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature
    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint
    """
    api_key = get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (
        f"{BASE_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url



if __name__ == "__main__":
    args = read_user_cli_args()
    query_url = build_weather_query(args.city, args.imperial)
    print(query_url)
