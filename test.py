import requests


def get_coordinates(place):
    url = f'https://api.tomtom.com/search/2/geocode/{place}.json'

    params = {
        'key': 'aGArnm6oXVRAGqBfiFCNpZaktp6OewMl',
        'query': place
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data['summary']['numResults'] > 0:
        coordinates = data['results'][0]['position']
        return coordinates
    else:
        print('Error occurred:', data['status'])
        return None
    
#     import requests


# def get_coordinates(place):
#     url = f'https://api.tomtom.com/search/2/geocode/{place}.json'

#     params = {
#         'key': 'aGArnm6oXVRAGqBfiFCNpZaktp6OewMl',
#         'query': place
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     if response.status_code == 200 and data['summary']['numResults'] > 0:
#         coordinates = data['results'][0]['position']
#         return coordinates
#     else:
#         print('Error occurred:', data['status'])
#         return None