import requests

pageNumber = "1"
url = f'https://unsplash.com/napi/search/photos?per_page={pageNumber}&query=enduro+mountain+bike&xp=semantic-search%3Aexperiment'

print(url)