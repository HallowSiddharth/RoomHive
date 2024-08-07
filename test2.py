import requests

# Replace with your TomTom API key
api_key = "YOUR_API_KEY"


# Function to get places from TomTom API
def get_places(query, lat, lon, radius=10000):
    url = "https://api.tomtom.com/search/2/poiSearch/{}.json".format(query)
    params = {"key": api_key, "lat": lat, "lon": lon, "radius": radius, "limit": 10}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Test the function
query = "restaurant"
latitude = 52.379189
longitude = 4.899431
radius = 5000  # 5 km radius

places = get_places(query, latitude, longitude, radius)
if places:
    for place in places["results"]:
        print(
            f"Name: {place['poi']['name']}, Address: {place['address']['freeformAddress']}"
        )
else:
    print("Error fetching places.")
