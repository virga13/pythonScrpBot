import os
import matplotlib.pyplot as plt
from PIL import Image
import requests
import json

def save_image(image_response, category, page, i):
    if not os.path.exists(category):
        os.makedirs(category)
    filename = f'{category}/image_{page}_{i}.jpg'
    with open(filename, 'wb') as f:
        f.write(image_response.content)
    print(f'Image {page}_{i} successfully downloaded.')
    return filename

def fetch_and_save_image(pageNumber, searchQuery):
    filenames = []
    searchQuery = "enduro+mountain+bike"
    for page in range(1, pageNumber + 1):
        url = f'https://unsplash.com/napi/search/photos?page={page}&per_page=10&query={searchQuery}&xp=semantic-search%3Aexperiment'
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            for i, result in enumerate(data['results']):
                image_url = result['urls']['small']
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_description = result['alt_description']
                    category = 'MTB' if 'mountain' in image_description else 'Cycling'
                    filename = save_image(image_response, category, page, i)
                    filenames.append(filename)
    return filenames

def display_images(filenames):
    for filename in filenames:
        img = Image.open(filename)
        plt.imshow(img)
        plt.show()

filenames = fetch_and_save_image(23, "enduro+mountain+bike")
display_images(filenames)