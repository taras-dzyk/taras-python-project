import http.client
import ssl
import json
from config import get_nasa_url, get_nasa_satellites_path

def get_satellites():
    conn = http.client.HTTPSConnection(get_nasa_url(), context = ssl._create_unverified_context())
    conn.request('GET', get_nasa_satellites_path())
    response = conn.getresponse().read().decode('utf-8')
    conn.close
    return json.loads(response)