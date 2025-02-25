import os, pathlib 
import pandas as pd
import numpy as np

def extract_metadata(path):
  metadata = pd.DataFrame(columns=["country", "image"])

  for folder in os.listdir(path):
    for file in os.listdir(f"{path}/{folder}"):
      row = pd.DataFrame({
          'country': [folder],
          'image': [pathlib.Path(f"{path}/{folder}/{file}")]
      })
      metadata = pd.concat([metadata, row], ignore_index = True)
  return metadata

metadata = extract_metadata('/kaggle/input/geolocation-geoguessr-images-50k/compressed_dataset')
metadata = metadata[metadata.groupby('country')['country'].transform('count').ge(500)]
msk = metadata.groupby('country')['country'].transform('size') >= 4000
metadata = pd.concat((metadata[msk].groupby('country').sample(n=4000), metadata[~msk]), ignore_index=True)
metadata.head()

COUNTRY_LIST = metadata['country'].unique().tolist()

def country_to_num(country):
  return COUNTRY_LIST.index(country)

def num_to_country(num):
  return COUNTRY_LIST[num]