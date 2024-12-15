import configparser
import os
from pathlib import Path

MAX_YEAR_LENGTH_KEY = "max_year_length"
NASA_URL_KEY = "nasa_url"
NASA_SATELLITES_API_PATH_KEY = "nasa_satellites_path"


def get_max_year_length():
    return get_config(MAX_YEAR_LENGTH_KEY)


def get_nasa_url():
    return get_config(NASA_URL_KEY)


def get_nasa_satellites_path():
    return get_config(NASA_SATELLITES_API_PATH_KEY)


def get_config(config_key):
    return read_config()[config_key]


def read_config():
    config = configparser.ConfigParser()
    root_dir = Path(__file__).parent.absolute()
    config.read(os.path.join(root_dir, "config.ini"))

    max_year_length_value = config.getint("General", MAX_YEAR_LENGTH_KEY)
    nasa_satellites_path = config.get("Satellites", NASA_SATELLITES_API_PATH_KEY)
    nasa_url = config.get("Satellites", NASA_URL_KEY)

    return {
        MAX_YEAR_LENGTH_KEY: max_year_length_value,
        NASA_SATELLITES_API_PATH_KEY: nasa_satellites_path,
        NASA_URL_KEY: nasa_url,
    }
