# Project Documentation: Web Scraping and Data Management in Python

## Project Overview:

This Python script is designed to fetch images from Unsplash based on a specific search query and save them locally on your machine. The code is divided into two main classes: ImageFetcher and ImageSaver.

ImageFetcher: This class is responsible for fetching images from Unsplash. It takes a base URL and a search query as input. The fetch_images method generates URLs for the Unsplash API, sends GET requests to these URLs, and processes the responses. For each image in the response, it extracts the image URL, sends another GET request to fetch the image, and extracts the image description. If the description contains the word 'mountain', it labels the image as 'MTB'; otherwise, it labels it as 'Cycling'. If no description is provided, it labels the image as 'null'. It then returns the image ID, description, and response as a tuple.

ImageSaver: This class is responsible for saving the fetched images locally. It maintains a dictionary filenames to keep track of the filenames of the saved images. The save_image method takes an image response, a description, a page number, and an image index as input, and saves the image in a directory named after the description. It generates a filename based on the description, page number, and image index, and writes the image content to this file. The save_images method takes a generator of image tuples and a page number as input, and saves each image using the save_image method. It also updates the filenames dictionary with the image ID and filename.

Finally, the script creates an instance of ImageFetcher with the base URL of Unsplash and a search query of 'enduro+mountain+bike', and an instance of ImageSaver. It then fetches 50 pages of images using the fetch_images method of ImageFetcher, and saves these images using the save_images method of ImageSaver.

## Coding Standards

Create Functions/Classes for scraping, saving information, etc


## Components:

1. **Image Fetching Module**: This module will handle the interaction with the website's API to fetch data. It will include functions to make API requests, parse the responses, and extract relevant information.

2. **Image Saving Module**: This module will define classes or functions to process the scraped data. It may involve filtering, cleaning, or transforming the data to make it suitable for storage and analysis.

3. **Data Storage Module**: This module will be responsible for saving the processed data. It could involve storing data in various formats, such as CSV files, JSON files, or a database.

4. **Database Management Module** (Optional): If a database is used for data storage, this module will handle database operations like creating tables, inserting data, querying data, and managing connections.
