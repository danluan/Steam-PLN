import pandas as pd
import time
import os
import json

DIR = 'datasets/reviews_cruas'

def get_file_list(dir):
    file_list = os.listdir(dir)
    return file_list


def get_steam_dataframe():
    df = pd.read_csv('teste.csv')

    for file_name in get_file_list(DIR)[:1]:
        if file_name.endswith('.json'):
            with open(f"{DIR}/{file_name}") as json_file:
                json_content = json.load(json_file)
                # fileJson = json.dumps(json.load(json_file)['reviews'], indent=2)
                # print(fileJson)
                # df = pd.DataFrame(columns=["recommendation_id", "author_steamid", "language", "review", "timestamp_created", "timestamp_updated"])
                # file_data = pd.json_normalize(json.load(json_file).T.reset_index(drop=True))
                file_data = pd.DataFrame.from_dict(json_content['reviews'], orient='index')
                df = pd.read_csv('teste.csv')
                df.head()
                df = pd.merge(df, file_data)
                # df = pd.concat(file_data, df)
                df.to_csv('teste.csv', index=False)
    return df


print(f"{len(get_file_list(DIR))} raw files")
get_steam_dataframe()

# steam_review_list = get_steam_review_json()
# df = pd.json_normalize(steam_review_list)
# df
