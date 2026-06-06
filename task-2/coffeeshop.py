import requests
import json

def fetch_data(url):
    r = requests.get(url)
    return r.text

def deserialize_data(raw_data):
    return json.loads(raw_data)

def get_data_from_key(data, key):
    return data.get(key)

def get_price(prices, item):
    return prices.get(item, 0)

def calculate_day(day_data, prices):
    total = 0
    
    drinks = day_data.get("drinks", {})
    for name, qty in drinks.items():
        total += qty * get_price(prices, name)
        
    desserts = day_data.get("desserts", {})
    for name, qty in desserts.items():
        total += qty * get_price(prices, name)
        
    total += day_data.get("tips", 0)
    return total

def calculate_week(data, prices):
    grand_total = 0
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    for day in days:
        day_data = get_data_from_key(data, day)
        if day_data:
            grand_total += calculate_day(day_data, prices)
            
    return grand_total
