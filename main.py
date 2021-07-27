import os
import json
import urllib.request

path_to_json = 'C:/Users/neeli/Downloads/neelima_dataset.json' # CHANGE THIS ACCORDING TO YOUR FILENAME AND LOCATION.

# READ THE DATASET FILE CONTAINING IMAGE LINKS
with open(path_to_json,'r') as f:
  data = json.load(f)

# CHANGE THIS TO WHERE YOU WANT TO SAVE THE FILES:
dir = 'C:/Users/neeli/Downloads/neelima_images/'

# CREATE THE DIRECTORY:
os.mkdir(dir)

for x in ['annotation','review']:

    # CREATE SUB-DIRECTORIES:
    os.mkdir(dir+ x + '/')

    c = 1

    # DOWNLOAD IMAGES
    for url in data[x]: # CHANGE THIS TO YOUR NAME
        urllib.request.urlretrieve(url, dir+x+'/'+url.split('/')[-1])
        print(c, " {} IMAGES DOWNLOADED SUCCESSFULLY!".format(str.upper(x)))
        c = c + 1
