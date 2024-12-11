import http.client
import ssl

def get_satellites():
    conn = http.client.HTTPSConnection("ssd-api.jpl.nasa.gov", context = ssl._create_unverified_context())
    conn.request("GET", "/sb_sat.api")
    data = conn.getresponse().read().decode('utf-8')
    return data