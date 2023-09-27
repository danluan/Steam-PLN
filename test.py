import pandas as pd
import os
import json

# todo
# read each file and write to a dataframe

def get_steam_review_json():
    steam_review_list = []
    dir = 'datasets/steam_reviews_cruas'
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.json'):
                with open(f"{root}/{file}") as json_file:
                    fileJson = json.load(json_file)
                    steam_review_list.append(fileJson)
    return steam_review_list

steam_review_list = get_steam_review_json()
df = pd.json_normalize(steam_review_list)
df

# def get_json_file():
#     with open('datasets/steam_reviews_cruas/Horror/Horror_123SlaughterMeStreet.json') as json_file:
#         fileJson = json.load(json_file)
#         print(fileJson['reviews'])

# get_json_file()

#get_steam_review_json()