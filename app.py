import datetime
import streamlit as st
import pandas as pd
from components.tweet import find_tweet
from components.db import db_insert
from components.export import to_csv, to_json

if 'search' not in st.session_state:
    st.session_state.search = False

if st.session_state.search == True:
    st.write(pd.read_csv("tweets.csv"))

st.sidebar.title("Twitter scraper using snscrape")

tags = st.sidebar.text_input('enter #hashtags separated by space', 'eg. tag1 tag2')

from_date = st.sidebar.date_input("from date", datetime.date(2023, 1, 1))

to_date = st.sidebar.date_input("to date", datetime.date(2023, 1, 1))

size = st.sidebar.slider('Limit no. of tweets (max 1000)', 0, 1000, 100)

if st.sidebar.button('search'):
    df = find_tweet(tags, from_date, to_date, size)
    df.to_csv("tweets.csv")
    st.write(df)
    st.session_state.search = True

if st.session_state.search == True:
    mongo_uri = st.sidebar.text_input('enter mongo uri', 'mongosrv://')
    collection = st.sidebar.text_input('enter collection name', 'collection_name')

    if st.sidebar.button('save to mongodb'): 
        if db_insert(mongo_uri, collection) is not True:
            st.sidebar.write("save unsucessful, invalid mongo uri")
        else:
            st.sidebar.write("saved to db")  

if st.session_state.search == True:
    st.sidebar.download_button(
        "Download as csv",
        to_csv(),
        "tweet_data.csv",
        "text/csv",
        key='download-csv'
    )

if st.session_state.search == True:
    st.sidebar.download_button(
        "Download as json",
        to_json(),
        "tweet_data.json",
        "text/json",
        key='download-json'
    )