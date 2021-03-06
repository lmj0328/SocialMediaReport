from flask import Flask, render_template, request, jsonify

from flask import request
from flask import Response
from flask import url_for
from flask import jsonify
import GetOldTweets3 as got
import pandas as pd
import datetime
import numpy as np
import requests
import json
from pyquery import PyQuery as pq

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/report', methods=['POST'])
def report():
    request_info = request.form.get("name")
    data = {}
    data["userInput"] = {}
    data["userInput"]["name"] = request_info
    data["numOfPost"] = {}
    data["numOfPost"]["total"] = 0
    data["numOfPost"]["instagram"] = 18
    data["numOfPost"]["facebook"] = 0

  
    ### error handling
    errorMessage = {
        "noUserInput": "Oops, you did not enter any username ...",
        "wrongTwitterInput": "Oops, the twitter account you enter either does not exist or has no content in it...",
        "wrongInstagramInput": "Oops, the Instagram username you enter either does not exist or is set to private...",
        "emptyInstagramContent": "Oops, your instagram account currently has no content..",
    }

    #TWITTER
    if request.form.get("twitter-input"): 
        twitter_info = request.form.get("twitter-input")
        data["userInput"]["twitterInput"] = twitter_info

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
        print(num_post)
        if num_post == 0:
            return render_template("error.html", data = errorMessage["wrongTwitterInput"])
        else:
            data["numOfPost"]["twitter"] = num_post
            data["numOfPost"]["total"] = num_post

    
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
        data["monthMostPost"] = {
            "month": most_month_verb,
            "total": month_posts_count,
            "facebook": 0,
            "twitter": month_posts_count,
            "monthPost":month_trend
        }

        # Twitter Total Like
        total_like = tweets_df.favorites.sum()
        total_like = format(total_like, ',')
        data["totalLikesTwitter"] = total_like


        # Twitter most like posts
        most_favorites_set = tweets_df[tweets_df.favorites == tweets_df.favorites.max()]
        most_fav_text = most_favorites_set.tweet_text.values[0]

        most_fav_date = most_favorites_set.date.values[0]
        most_fav_date = pd.to_datetime(str(most_fav_date ))
        most_fav_date = most_fav_date.strftime('%Y.%m.%d')

        data["twitterPostWithMostLikes"] = {
            "content":most_fav_text,
            "date": most_fav_date,
            "twitterAccount": "@" + twitter_info
        }

        # The latest post
        tweets_df['hour'] = tweets_df.date.dt.hour
        pos = tweets_df.hour.sub(3).abs().values.argmin()
        df1 = tweets_df.iloc[[pos]]
        latest_text = df1.tweet_text.values[0]
        latest_date = df1.date.values[0]
        latest_date = pd.to_datetime(str(latest_date))
        latest_date = latest_date.strftime('%Y.%m.%d')
        if df1.hour.values[0] < 5 or df1.hour.values[0] > 20:
            latest_hour = (str(df1.hour.values[0]), ':00')
            latest_hour = "".join(latest_hour)
            data["twitterLatestPost"] = {
                "latePost": bool(True),
                "content":latest_text,
                "date":latest_date,
                "time":latest_hour,
                "twitterAccount": "@" + twitter_info
            }
        else:
            data["twitterLatestPost"] = {
                "latePost": bool(False)
            }


        #Mention Most
        tweets_df['mentions'].replace('', np.nan, inplace=True)
        tweets_df.dropna(subset=['mentions'], inplace=True)
        mention_set = tweets_df.groupby(['mentions']).size().reset_index(name='counts')
        mention_set.sort_values(by=['counts'], inplace=True, ascending=False)
        if mention_set.shape[0] > 3:
            mention_set = mention_set.iloc[:3]
        mention_name = mention_set.mentions.tolist()
        mention_counts = mention_set.counts.tolist()
        data["twitterPeopleMentionedMost"] = {
            "names":mention_name
        }
        data["twitterPeopleMentioneTimes"] = {
            "top_times":mention_counts
        }

        # Tweet first post
        tweet_arrange = tweets_df.sort_values(by = ['date'])
        first_tweet = tweet_arrange.iloc[[0]]
        first_text = first_tweet.tweet_text.values[0]
        first_date = first_tweet.date.values[0]
        first_date = pd.to_datetime(str(first_date))
        first_date = first_date.strftime('%Y.%m.%d')
        data["twitterFirstPostYear"] = {
            "content":first_text,
            "date": first_date,
            "twitterAccount": "@" + twitter_info
        }

        # Tweet last post
        last_tweet = tweet_arrange.iloc[[-1]]
        last_text = last_tweet.tweet_text.values[0]
        last_date = last_tweet.date.values[0]
        last_date = pd.to_datetime(str(last_date))
        last_date = last_date.strftime('%Y.%m.%d')
        data["twitterLastPostYear"] = {
            "content":last_text,
            "date": last_date,
            "twitterAccount": "@" + twitter_info
        }

        # Hashtags
        tweets_df['hashtags'].replace('', np.nan, inplace=True)
        tweets_df.dropna(subset=['hashtags'], inplace=True)
        hash_set = tweets_df.groupby(['hashtags']).size().reset_index(name='counts')
        hash_set.sort_values(by=['counts'], inplace=True, ascending=False)
        hash_name = hash_set.hashtags.tolist()
        hash_counts = hash_set.counts.tolist()
        if len(hash_name) == 0: 
            data["twitterHashtag"] = {
                "hashtag": bool(False)
            }
        else:
            hash_most = hash_name[0]
            hash_most
            data["twitterHashtag"] = {
                "hashtag": bool(True),
                "hashtags":hash_name,
                "hashtagsCount": hash_counts,
                "hashtagMost": hash_most
            }


    else: 
        twitter_info = bool(False)
        data["userInput"]["twitterInput"] = bool(False)
        

    ## FACEBOOK
    if request.form.get("facebook-input"): 
        facebook_info = request.form.get("facebook-input")
    else: 
        facebook_info = bool(False)
        data["userInput"]["facebookInput"] = bool(False)

    ## INSTAGRAM
    if request.form.get("instagram-input"): 
        instagram_info = request.form.get("instagram-input")
        ins_user = instagram_info
        url = ("https://www.instagram.com/", ins_user, '/')
        url = "".join(url)
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        #     'cookie': 'mid=W4VyZwALAAHeINz8GOIBiG_jFK5l; mcd=3; csrftoken=KFLY0ovWwChYoayK3OBZLvSuD1MUL04e; ds_user_id=8492674110; sessionid=IGSCee8a4ca969a6825088e207468e4cd6a8ca3941c48d10d4ac59713f257114e74b%3Acwt7nSRdUWOh00B4kIEo4ZVb4ddaZDgs%3A%7B%22_auth_user_id%22%3A8492674110%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%228492674110%3Avsy7NZ3ZPcKWXfPz356F6eXuSUYAePW8%3Ae8135a385c423477f4cc8642107dec4ecf3211270bb63eec0a99da5b47d7a5b7%22%2C%22last_refreshed%22%3A1535472763.3352122307%7D; csrftoken=KFLY0ovWwChYoayK3OBZLvSuD1MUL04e; rur=FRC; urlgen="{\"103.102.7.202\": 57695}:1furLR:EZ6OcQaIegf5GSdIydkTdaml6QU"'
        }

        def get_urls(url):
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
                else:    
                    print('error code：', response.status_code)
                    return True

            except Exception as e:
                print(e)
                return None

        html = get_urls(url)
        if (html == True):
            return render_template("error.html", data = errorMessage["wrongInstagramInput"])
        else:
            urls = []
            doc = pq(html)
            items = doc('script[type="text/javascript"]').items()   
            for item in items:
                if item.text().strip().startswith('window._sharedData'):
                    js_data = json.loads(item.text()[21:-1], encoding='utf-8')
                    edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
                    for edge in edges:
                        url = edge['node']['display_url']
                        urls.append(url)

            if urls == []:
                return render_template("error.html", data = errorMessage["emptyInstagramContent"])
            else:
                data["userInput"]["instagramInput"] = instagram_info
                data["insPostMostComments"] = {
                    "pictureLink": ["picture here"],
                    "comments": ["comment1", "comment2", "comment3", "comment4"],
                    "totalComments": 12
                }
                data["insNinephotos"] = urls
    else: 
        instagram_info = bool(False)
        data["userInput"]["instagramInput"] = bool(False)

    
    # if no user input for social media
    if (not twitter_info) and (not instagram_info) and (not facebook_info):
        return render_template("error.html", data = errorMessage["noUserInput"])
    else:
        #Incoming data is processed here and converted into following format:
        data["year"] = 2019
        data["facebookNumOfFriends"] = 423
        data["facebookRecentAcademic"] = {
            "schoolName":"Texas Academy of Mathematics and Technology",
            "year":2019
        }
        return render_template("samplereport.html", data = data)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
