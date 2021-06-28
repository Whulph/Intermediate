# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:27:33 2021

@author: Tyler
"""

import requests as reqs
 
url = "https://images-api.nasa.gov/search"
 
params = {
    "q": "apollo",
    "page": "1",
    "media_type": "image",
    "year_start": "2018",
    "year_end": "2020"
}
 
response = reqs.get(url, params=params)
response.raise_for_status()
 
images = response.json()["collection"]["items"]
print(f"Number of images: {len(images)}")
for image in images:
    thumbnail_url = image["links"][0]["href"]
    image_url = thumbnail_url[:thumbnail_url.rfind("~")] + "~orig.jpg"
    print(image_url)