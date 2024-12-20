import requests

def get_weather(city):
    
    api_key = '836e7753abfaea941cca25c329b4de9e'
    
    base_url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}"
    
    
    params = {"q": city, "appid": api_key, "units": "metric"}

    
    response = requests.get(base_url, params=params)

    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Condition": data["weather"][0]["description"],
        }
        return weather
    else:
        return {"Error": "City not found!"}

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if "Error" in weather:
        print(weather["Error"])
    else:
        print(f"City: {weather['City']}")
        print(f"Temperature: {weather['Temperature']}°C")
        print(f"Humidity: {weather['Humidity']}%")
        print(f"Condition: {weather['Condition'].capitalize()}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
