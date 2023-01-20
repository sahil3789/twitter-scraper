import pandas as pd 
import snscrape.modules.twitter as sntwitter

def find_tweet(tags, from_date, to_date, n_tweet):

    query = get_query(tags, from_date, to_date)

    attributes_container = []
    max_tweet = n_tweet

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):

        if i>max_tweet:
            break

        attributes_container.append([
                                     tweet.date,
                                     tweet.id,
                                     tweet.user.username,
                                     tweet.url,
                                     tweet.rawContent,
                                     tweet.replyCount,
                                     tweet.retweetCount,
                                     tweet.lang,
                                     tweet.sourceLabel,
                                     tweet.likeCount,
                                     tweet.hashtags
                                     ])

    return pd.DataFrame(attributes_container, columns=["date",
                                                       "tweet id",
                                                       "username",
                                                       "url",
                                                       "content",
                                                       "Reply_Count",
                                                       "Retweet_Count",
                                                       "Lang",
                                                       "Label",
                                                       "Like_Count",
                                                       "hashtag"
                                                    ]).sort_values("date",ascending=False)

def get_query(tags, from_date, to_date):
    tag_list = tags.split()
    for i in range(len(tag_list)):
        tag_list[i] = "#"+tag_list[i]
    t = " OR ".join(tag_list)    
    return "(" + t + ")" + " since:"+ str(from_date) + " until:" + str(to_date)