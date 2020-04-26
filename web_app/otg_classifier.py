import pandas as pd
from pickle import load
import praw
import util
import sys
from praw.models import MoreComments

punctuationRe = util.punctuationRe
symbolsRe = util.symbolsRe
URLRe = util.URLRe
makeString = util.makeString
removePunctuation = util.removePunctuation
removeSymbols = util.removeSymbols
removeURLs = util.removeURLs

def predictIt(url):
    model = load(open('/home/anton/Documents/Flair_detector/model/svm_71.pkl','rb'))
    # loaded_model = pickle.load(open(filename, 'rb'))
    reddit = praw.Reddit(client_id='HcjyI-VCKlu3pQ',client_secret = '5igSrCH2dvgW3VZ8XbRIJr4ZQsI',user_agent='scrape_reddit')
    print(model)

    sub = praw.models.Submission(reddit,url = url)
    title = sub.title
    body = sub.selftext
    comments = ''
    if isinstance(sub.comments, MoreComments):
        comments = ''
        totalPost = title + ' ' + body
    else:
        sub.comments.replace_more(limit=None)
        for comment in sub.comments:
            comments += comment.body + ' '
        totalPost = title + ' ' + body + ' ' + comments

    totalPost = removePunctuation(totalPost)
    totalPost = removeSymbols(totalPost)
    totalPost = removeURLs(totalPost)

    return model.predict([totalPost])[0],sub.link_flair_text
