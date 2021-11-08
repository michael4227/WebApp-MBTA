# Useful URLs (you need to add the appropriate parameters for your requests)
from pprint import pprint


MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "S702YQUN9ATGvZu3GmhQAcnoU9YH45AG"
MBTA_API_KEY = "5d64f7ac5dda4699ad94b4d17d14f22f"
#michael



# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib.request
    import json
    from pprint import pprint

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)

# myapi = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Washington,DC'
# get_json(myapi)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    address = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    import urllib.request
    import json
    f = urllib.request.urlopen(address)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    dic_LatLng = response_data['results'][0]['locations'][0]['displayLatLng']
    LatLng = (dic_LatLng['lat'], dic_LatLng['lng'])
    return LatLng

# place_name = 'MFA,Boston'
# get_lat_long(place_name)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    address = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    import urllib.request
    import json
    from pprint import pprint
    f = urllib.request.urlopen(address)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    filtered = response_data['data'][0]['attributes']
    for k in filtered:
        if filtered['wheelchair_boarding'] == 1:
            wheelchair_accessible = 'wheelchair boarding accessible'
        elif filtered['wheelchair_boarding'] == 0:
            wheelchair_accessible = 'wheelchair boarding no info.'
        elif filtered['wheelchair_boarding'] == 2:
            wheelchair_accessible = 'wheelchair boarding inaccessible'
    dic_station_wheelchair = (filtered['name'], wheelchair_accessible)
    return dic_station_wheelchair

# lat = 42.35899
# lon = -71.05863
# pprint(get_nearest_station(lat, lon))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    tuple_latlng = get_lat_long(place_name)
    lat = tuple_latlng[0]
    lng = tuple_latlng[1]
    dic_st_wl = get_nearest_station(lat, lng)
    nearest_MBTA = dic_st_wl[0]
    wheelchair = dic_st_wl[1]
    print(f'The nearest MBTA stop is {nearest_MBTA}, and it\'s {wheelchair}')

# print(find_stop_near('MFA,Boston'))


def main():
    """
    You can test all the functions here
    """
    myapi = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Washington,DC'
    get_json(myapi)
    place_name = 'MFA,Boston'
    get_lat_long(place_name)
    lat = 42.35899
    lon = -71.05863
    print(get_nearest_station(lat, lon))
    find_stop_near('MFA,Boston')

if __name__ == '__main__':
    main()