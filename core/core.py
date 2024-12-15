import pprint
from satellites import get_satellites as call_get_satellites


def pretty_print(obj):
    pprinter = pprint.PrettyPrinter(depth=3)
    pprinter.pprint(obj)


def get_all_satellites():
    return call_get_satellites()


def get_satellites_for_year(year):
    satellites = call_get_satellites()
    satellites_for_year = [sat for sat in satellites if sat["sat"]["prov_year"] == year]
    return satellites_for_year
