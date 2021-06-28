# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:48:09 2021

@author: Tyler
"""

# matplotlib inline
import matplotlib.pyplot as plt
from skimage import io
import os
import pprint
import requests as reqs
import json

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

payload = {'api_key': "DEMO_KEY",
           'sol': 1000}

response = reqs.get(rover_url, params=payload)
response_dictionary = response.json()
photos = response_dictionary['photos']
print(type(photos))
print(len(photos))
print(photos[0])
url_photos = list()
for photo in photos:
    url_photos.append(photo['img_src'])

print(url_photos[0])

import random
url_pictures = random.sample(url_photos, 20)
fig, axes = plt.subplots(4, 5, figsize=(20, 20))
ax = axes.ravel()

for i in range(20):
    ax[i].imshow(io.imread(url_pictures[i]))

fig.tight_layout()