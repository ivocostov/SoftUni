"""
API for searching news over the web
"""

import requests

# API endpoint

url = 'http://newsapi.org/v2/top-headlines?country=us&apiKEY=e0b4c462dc3d41548b8bcb0afb1aeb08'

# Make request to the API
response = requests.get(url)

# Get the response data as python object
news_data = response.json()


articles_counter = 1

for article in news_data['articles']:
    if articles_counter < 50:
        print(f"{articles_counter}: {article['title']}")
        articles_counter += 1

    else:
        break