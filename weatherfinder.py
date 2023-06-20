import requests
import json

def get_weather(city):
    # Enter your OpenWeatherMap API key here
    api_key = "YOUR_API_KEY"

    # API endpoint URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Parse the JSON data from the response
        data = json.loads(response.text)

        # Extract relevant weather information
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

        # Return the weather information
        return weather
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        print("Error:", e)
        return None

# Example usage
city = input("Enter city name: ")
weather_info = get_weather(city)

if weather_info:
    print("\nWeather Information for", weather_info["city"])
    print("Temperature:", weather_info["temperature"], "K")
    print("Description:", weather_info["description"])
    print("Humidity:", weather_info["humidity"], "%")
    print("Wind Speed:", weather_info["wind_speed"], "m/s")