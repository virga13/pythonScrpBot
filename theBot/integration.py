import os
import requests
import json
import logging

class ImageFetcher:
    def __init__(self, base_url, search_query):
        self.base_url = base_url
        self.search_query = search_query

    def fetch_images(self, page_number):
        for page in range(1, page_number + 1):
            url = self.build_url(page)
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                for i, result in enumerate(data['results']):
                    image = self.parse_image(result)
                    if image:
                        yield image

    def build_url(self, page):
        return f'{self.base_url}/napi/search/photos?page={page}&per_page=10&query={self.search_query}&xp=semantic-search%3Aexperiment'
                  
    def parse_image(self, result):
        image_url = result['urls']['small']
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_description = result['alt_description']
            if image_description is not None:
                  description = 'MTB' if 'mountain' in image_description else 'Cycling'
            else:
                description = "null"   
            image_id = result['id']
            return image_id, description, image_response
        else:
            logging.error(f"Failed to fetch image: {image_response.status_code}")
            return None

class ImageSaver:
    filenames = {}

    @staticmethod
    def save_image(image_response, description, page, i):
        if not os.path.exists(description):
            os.makedirs(description)
        filename = f'{description}/image_{page}_{i}.jpg'
        with open(filename, 'wb') as f:
            f.write(image_response.content)
        print(f'Image {page}_{i} successfully downloaded.')
        return filename

    @classmethod
    def save_images(cls, images, page):
        for i, (image_id, description, image_response) in enumerate(images):
            filename = cls.save_image(image_response, description, page, i)
            cls.filenames[image_id] = filename

fetcher = ImageFetcher("https://unsplash.com", "enduro+mountain+bike")
fetcher2 = ImageFetcher("https://unsplash.com", "mountain+bike")

images = fetcher.fetch_images(50)
images2 = fetcher2.fetch_images(40)
ImageSaver.save_images(images, 1)