from django.shortcuts import render
import pandas as pd
import requests

def index(request):
    df = pd.read_csv("worldcities.csv")
    
    if "city" in request.GET:
        city = request.GET["city"] 
    
        if df[df["city_ascii"] == city]["city_ascii"].any(): 
            lat = df[df["city_ascii"] == city]["lat"] 
            lon = df[df["city_ascii"] == city]["lng"]
  
            url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"
            querystring = {"unit_system": "si", "fields": ["precipitation", "precipitation_type", "temp", "cloud_cover", "wind_speed", "weather_code"], "lat": lat, "lon": lon}
            headers = {'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com", 'x-rapidapi-key': "61c876efa0mshd690e18287bd83ap11b3f0jsna76b1f2bcc4c"
                       }
            response = requests.request("GET", url, headers=headers, params=querystring).json()
    
            context = {"city_name": city, "temp": response["temp"]["value"], "weather_code": response["weather_code"]["value"], "wind_speed": response["wind_speed"]["value"], "precipitation_type": response["precipitation_type"]["value"]}
    
        else:
            context = None
    
    else:
        context = None 
        

    return render(request, "weather/index.html", context)



