from flask import Flask, render_template, request, jsonify

from flask import request
from flask import Response
from flask import url_for
from flask import jsonify

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
            "total": 56, 
            "twitter": 32, 
            "instagram": 18,
            "facebook": 6
        },
        "monthMostPost": {
            "month": "JAN",
            "total": 15,
            "facebook": 0,
            "twitter": 15,
            "monthPost":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        },
        "totalLikesTwitter": 78,
        "twitterPostWithMostLikes": {
            "content":"Thank you everyone....",
            "date":"Jun.29, 2019",
            "twitterAccount": "rocketrystars"
        },
        "twitterLatestPost":{
            "content":"Meet Sarah....",
            "date":"Jan.30, 2019",
            "time":"3 a.m.",
            "twitterAccount": "rocketrystars"
        },
        "twitterPeopleMentionedMost": {
            "RocketContest":3,
            "katyperry": 2,
            "spotify": 1
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
