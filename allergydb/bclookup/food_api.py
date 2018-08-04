import requests

def get_by_barcode(barcode):
    base_url = 'https://api.edamam.com/api/food-database/parser'
    query_str = {
        'upc': barcode,
        'app_id': 'b97689a7',
        'app_key': '6e9420e9017487ad8e83ba8d3acf10dc',
    }
    response = requests.get(base_url, query_str)
    return response.json()

def get_by_name(name):
    base_url = 'https://api.edamam.com/api/food-database/parser'
    query_str = {
        'ingr': name,
        'app_id': 'b97689a7',
        'app_key': '6e9420e9017487ad8e83ba8d3acf10dc',
    }
    response = requests.get(base_url, query_str)
    return response.json()

def get_recipes(search, health):
    base_url = 'https://api.edamam.com/search'
    query_str = {
        'q': search,
        'health': health,
        'app_id': 'f7240714',
        'app_key': '539df2776c0da7437acaa792a240366a',
    }
    response = requests.get(base_url, query_str)
    return response.json()
