import tweepy
from textblob import TextBlob
import csv

# authentication

coms_key = 'comsumer_key'
coms_secret = 'comsumer_secret_key'

access_token = 'Enter your access token'
access_token_sceret = 'Enter access token secret'

auth = tweepy.OAuthHandler(coms_key, coms_secret)
auth.set_access_token(access_token, access_token_sceret)

api = tweepy.API(auth)

tweets = api.search('trump', count=100)

# it is just to search many query at once
# you can ignore it

print('enter the query you wish tweets for')
i = {}
i = TextBlob(input())
y = i.words

# this looop is to itrerate over our array created above

for n in y:
    tweets = api.search(n, count=10)
    countn = 0
    countp = 0
    i = 0
    with open('tweets.csv', 'a', encoding='utf-8') as datas:
        csvwriter = csv.writer(datas)
        csvwriter.writerow(
            [f'*********************************    {n}     ********************************************'])
        csvwriter.writerow(['polarity', 'tweets', 'username'])
        for tweet in tweets:
            if tweet_analysor(tweet) == 'negative':
                csvwriter.writerow([tweet_analysor(tweet), tweet.text, tweet.user.screen_name])
                countn += 1
            elif tweet_analysor(tweet) == 'positve':
                csvwriter.writerow([tweet_analysor(tweet), tweet.text, tweet.user.screen_name])
                countp += 1
            else:
                csvwriter.writerow(['netral', tweet.text, tweet.user.screen_name])
                i += 1
    print(f'{countn} tweeets are of negative polarity {n}')
    print(f'{countp} tweeets are of postive polarity {n}')
    print(f'{i} tweeets are of neutral polarity {n}')
    print('successful get tweets on {}'.format(n))

print('done')