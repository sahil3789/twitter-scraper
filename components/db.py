from pymongo import MongoClient
import pandas as pd
import json

def db_insert(uri,collection_name):
    try:    
        df = pd.read_csv("tweets.csv",lineterminator='\n')
        df.reset_index(inplace=True)
        client = MongoClient(uri)
        tweet = client.tweet
        tweet[collection_name].insert_many(json.loads(df.T.to_json()).values())
        return True
    except:
        return False    