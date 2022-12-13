import re

text = input()
travel_points = 0
travel_destinations = []

pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.findall(pattern, text)

for destination in result:
    travel_destinations.append(destination[1])
    travel_points += len(destination[1])

print(f"Destinations: {', '.join(travel_destinations)}")
print(f"Travel Points: {travel_points}")