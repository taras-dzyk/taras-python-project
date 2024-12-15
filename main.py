from core import (
    get_all_satellites,
    get_satellites_for_year,
    is_valid_year,
    pretty_print,
)

year = input("Please enter year to inspect. Type 'all' for all the years: ")

if not is_valid_year(year):
    print("Please enter year in a format like: '2012': ")
    year = input("Please enter year to inspect. Type 'all' for all the years: ")


if not is_valid_year(year):
    print("Incorrect input")
elif year == "all":
    print("Getting data for all the years")
    satellites = get_all_satellites()
    pretty_print(satellites)
else:
    print(f"Getting data for: {year}")
    satellites_for_year = get_satellites_for_year(year)
    pretty_print(satellites_for_year)
