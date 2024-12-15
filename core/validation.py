from config import get_max_year_length


def is_valid_year(year):
    return year == "all" or (year.isnumeric() and len(year) == get_max_year_length())
