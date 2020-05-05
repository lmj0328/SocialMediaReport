from flask import Flask, render_template, request, jsonify

from flask import request
from flask import Response
from flask import url_for
from flask import jsonify
import GetOldTweets3 as got
import pandas as pd
import datetime
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/report', methods=['POST'])
def report():
    request_info = request.form.get("name")
    if request.form.get("twitter-input"): 
        twitter_info = request.form.get("twitter-input")
    else: 
        twitter_info = bool(False)

    if request.form.get("facebook-input"): 
        facebook_info = request.form.get("facebook-input")
    else: 
        facebook_info = bool(False)

    if request.form.get("instagram-input"): 
        instagram_info = request.form.get("instagram-input")
    else: 
        instagram_info = bool(False)

    #data scraping
    username = twitter_info
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                        .setSince("2019-01-01")\
                                        .setUntil("2019-12-31")\
                                        .setEmoji("unicode")
    tweet_df = pd.DataFrame({'got_criteria':got.manager.TweetManager.getTweets(tweetCriteria)})
    tweets_df = pd.DataFrame()
    def get_twitter_info():
        tweets_df["tweet_text"] = tweet_df["got_criteria"].apply(lambda x: x.text)
        tweets_df["date"] = tweet_df["got_criteria"].apply(lambda x: x.date)
        tweets_df["hashtags"] = tweet_df["got_criteria"].apply(lambda x: x.hashtags)
        tweets_df["link"] = tweet_df["got_criteria"].apply(lambda x: x.permalink)
        tweets_df["favorites"] = tweet_df["got_criteria"].apply(lambda x: x.favorites)
        tweets_df["retweets"] = tweet_df["got_criteria"].apply(lambda x: x.retweets)
        tweets_df["mentions"] = tweet_df["got_criteria"].apply(lambda x: x.mentions)
    get_twitter_info()
    tweets_df['mentions'] = tweets_df['mentions'].astype(str)
    
    # Data Aggregation
    # Number of posts
    num_post = tweets_df.shape[0]

    #Month  with most post
    tweets_df['month'] = pd.DatetimeIndex(tweets_df['date']).month
    month_posts = tweets_df.groupby(['month']).size().reset_index(name='counts')
    most_month_val = month_posts[month_posts.counts == month_posts.counts.max()]
    most_month = most_month_val.month.values[0]
    month_posts_count = most_month_val.counts.values[0]
    most_month_verb = datetime.date(1900, most_month, 1).strftime('%B')
    month_posts.index = month_posts.month
    df2 = pd.DataFrame({'month':range(1, 13), 'counts':0})
    df2.index = df2.month
    df2.counts = month_posts.counts
    df2= df2.fillna(0)
    df2.drop('month',1).reset_index()
    month_trend =  df2.counts.tolist()

    # Twitter Total Like
    total_like = tweets_df.favorites.sum()
    total_like = format(total_like, ',')

    # Twitter most like posts
    most_favorites_set = tweets_df[tweets_df.favorites == tweets_df.favorites.max()]
    most_fav_text = most_favorites_set.tweet_text.values[0]

    most_fav_date = most_favorites_set.date.values[0]
    most_fav_date = pd.to_datetime(str(most_fav_date ))
    most_fav_date = most_fav_date.strftime('%Y.%m.%d')

    # The latest post
    tweets_df['hour'] = tweets_df.date.dt.hour
    pos = tweets_df.hour.sub(3).abs().values.argmin()
    df1 = tweets_df.iloc[[20]]
    latest_text = df1.tweet_text.values[0]
    latest_date = df1.date.values[0]
    latest_date = pd.to_datetime(str(latest_date))
    latest_date = latest_date.strftime('%Y.%m.%d')
    latest_hour = (str(df1.hour.values[0]), ':00')
    latest_hour = "".join(latest_hour)

    #Mention Most
    tweets_df['mentions'].replace('', np.nan, inplace=True)
    tweets_df.dropna(subset=['mentions'], inplace=True)
    mention_set = tweets_df.groupby(['mentions']).size().reset_index(name='counts')
    mention_set.sort_values(by=['counts'], inplace=True, ascending=False)
    if mention_set.shape[0] > 3:
        mention_set = mention_set.iloc[:3]
    mention_name = mention_set.mentions.tolist()
    mention_counts = mention_set.counts.tolist()

    #Incoming data is processed here and converted into following format:
    data = {
        "year": 2019,
        "userInput": {
            "name": request_info,
            "twitterInput": twitter_info,
            "facebookInput": facebook_info,
            "instagramInput": instagram_info
        },
        "numOfPost": {
            "total": num_post + 18 + 6, 
            "twitter": num_post, 
            "instagram": 18,
            "facebook": 6
        },
        "monthMostPost": {
            "month": most_month_verb,
            "total": month_posts_count,
            "facebook": 0,
            "twitter": month_posts_count,
            "monthPost":month_trend
        },
        "totalLikesTwitter": total_like,
        "twitterPostWithMostLikes": {
            "content":most_fav_text,
            "date": most_fav_date,
            "twitterAccount": twitter_info
        },
        "twitterLatestPost":{
            "content":latest_text,
            "date":latest_date,
            "time":latest_hour,
            "twitterAccount": twitter_info
        },
        "twitterPeopleMentionedMost": {
            "names":mention_name
        },
        "twitterPeopleMentioneTimes": {
            "top_times":mention_counts
        },
        "insPostMostComments": {
            "pictureLink": ["picture here"],
            "comments": ["comment1", "comment2", "comment3", "comment4"],
            "totalComments": 12
        },
        "insNinephotos": [
            "pictureLink1",
            "pictureLink2",
            "pictureLink3",
            "pictureLink4",
            "pictureLink5",
            "pictureLink6",
            "pictureLink7",
            "pictureLink8",
            "pictureLink9"
        ],
        "facebookNumOfFriends": 423,
        "facebookRecentAcademic": {
            "schoolName":"Texas Academy of Mathematics and Technology",
            "year":2019
        }
    }
    return render_template("samplereport.html", data = data)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
