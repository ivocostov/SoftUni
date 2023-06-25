def forecast(*args):
    result = []

    def locations_weather(weather_type):
        cities = []

        for city, weather in args:
            if weather == weather_type:
                cities.append(city)

        for location in sorted(cities):
            result.append(f"{location} - {weather_type}")


    locations_weather('Sunny')
    locations_weather('Cloudy')
    locations_weather('Rainy')

    return '\n'.join(result)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

