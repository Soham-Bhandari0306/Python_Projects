import requests

city = input("Enter city name: ")

api_key = "b04d4aa18982c2dc41a3beaca2397713"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Details")
    print("----------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Condition:", condition)
    print("Humidity:", humidity, "%")
else:
    print("City not found! Please check the name.")