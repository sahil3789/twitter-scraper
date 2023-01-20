import pandas as pd

def to_csv():
   return pd.read_csv("tweets.csv").to_csv(index=False).encode('utf-8')
   
def to_json():
    return pd.read_csv("tweets.csv").to_json(orient="index").encode('utf-8')
