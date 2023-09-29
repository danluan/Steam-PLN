import pandas as pd
import time
import os
import json

DIR = 'datasets/reviews_cruas'

def get_folders_list(dir):
    folders_list = os.listdir(dir)
    return folders_list

def get_files(dir):
    file_list = os.listdir(dir)
    return file_list

def get_file_content(file_name):
    with open(f"{file_name}") as json_file:
        json_content = json.load(json_file)
        json_reviews = json_content['reviews']
        print(type(json_reviews))
        for review in json_reviews:
            for key in json_reviews[review]:
                item = json_reviews[review][key]
                if key == 'author':
                    for author_key in json_reviews[review][key]:
                        author_item = json_reviews[review][key][author_key]
                        print(f"author_{author_key} : {author_item}")
                else:
                    print(f"{key} : {item} ")

def get_steam_dataframe():
    for file_name in get_file_list(DIR)[5:]:
        if file_name.endswith('.json') and file_name.startswith('FPS'):
            temp = pd.read_csv('teste.csv')
            with open(f"{DIR}/{file_name}") as json_file:
                json_content = json.load(json_file)
                file_data = pd.DataFrame.from_dict(json_content['reviews'], orient='index')
                temp = pd.concat([file_data, temp])
                # df = pd.concat(file_data, df)
            temp.to_csv('teste.csv', index=False)
            print(f"File {file_name} ")
    pass



def get_file_names_list():
    folders_list = get_folders_list(DIR)
    file_names_list = []
    for folder in folders_list:
        file_names_list.append(get_files(f"{DIR}/{folder}/"))
        print(get_files(f"{DIR}/{folder}/"))
    return file_names_list

def main():
    files_list = get_file_names_list()
    for file_name in files_list:
        if file_name.endswith('.json'):
            with open(f"{DIR}/{folder}/{file_name}") as json_content:
                json_data = json.loads(json_content.read())
                json_data_frame2 = pd.DataFrame.from_dict(json_data['reviews'], orient='index')
                   #print(json_data_frame2)
        print(f"File {file_name} read")
    print(f"Folder {folder} read")
        

files_list = []

meta_col = [
    "recommendationid",
    "author_steamid",
    "author_num_games_owned",
    "author_num_reviews",
    "author_playtime_forever",
    "author_playtime_last_two_weeks",
    "author_playtime_at_review",
    "author_last_played",
    "language",
    "review",
    "timestamp_created",
    "timestamp_updated",
    "voted_up",
    "votes_up",
    "votes_funny",
    "weighted_vote_score",
    "comment_count",
    "steam_purchase",
    "received_for_free",
    "written_during_early_access",
]

# print(f"{len(get_file_list(DIR))} raw files")
# get_file_content('review_sample.json')
# get_steam_dataframe()

# steam_review_list = get_steam_review_json()
# df = pd.json_normalize(steam_review_list)
# df