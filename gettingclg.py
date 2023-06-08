import requests
import random
import pandas as pd,openpyxl

def get_coordinates(api_key, query):
    
    url = 'https://api.tomtom.com/search/2/geocode/{query}.json'
    
    
    params = {
        'key': api_key,
        'query': query
    }
    
    
    response = requests.get(url, params=params)
    data = response.json()
    
    
    if response.status_code == 200 and data['summary']['numResults'] > 0:
        coordinates = data['results'][0]['position']
        return coordinates
    else:
        print('Error occurred:', data['status'])
        return None

def get_nearby_hotels(api_key, latitude, longitude, radius=10000, limit=10):
    
    url = 'https://api.tomtom.com/search/2/search/hotel.json'
    

    params = {
        'key': api_key,
        'lat': latitude,
        'lon': longitude,
        'radius': radius,
        'limit': limit
    }
    
    
    response = requests.get(url, params=params)
    data = response.json()
    
    
    if response.status_code == 200 and data['summary']['numResults'] > 0:
        hotels = data['results']
        return hotels
    else:
        print('Error occurred:', data['status'])
        return []


api_key = 'aGArnm6oXVRAGqBfiFCNpZaktp6OewMl'


college = 'SRM KATTANKULATHUR'


coordinates = get_coordinates(api_key, college)

if coordinates:
    latitude = coordinates['lat']
    longitude = coordinates['lon']

    
    hotels = get_nearby_hotels(api_key, latitude, longitude)

    hotel_list=[]
    choices=['yes','no']
    for hotel in hotels:
        hotel_dict={}
        hotel_dict['Name']=hotel['poi']['name']
        hotel_dict['Address']=hotel['address']['freeformAddress']
        hotel_dict['Price']=random.randint(1000,10000)
        hotel_dict['AC']=random.choice(choices)
        hotel_dict['Food']=random.choice(choices)
        hotel_dict['Occupancy']=random.randint(1,6)
        hotel_list.append(hotel_dict)
        df = pd.DataFrame(hotel_list)
        df.to_excel('hotels_list.xlsx', index=False)
        df.to_csv('hotels_list.csv', index=False)
        print('Name:', hotel['poi']['name'])
        print('Address:', hotel['address']['freeformAddress'])
        print('---')
