import csv
import tweepy
from tweepy import OAuthHandler

consumer_key = 'bHLXKj7wSn2UH5yfLceg7wW53'
consumer_secret = 'SXPcfKzfhVBU5WGxYwqyTVBgd0qourrd6IsUy97I4b6rC4d68t'
access_token = '613251570-LeuCjbeYz7CcmwOW9F5MkH9gotumw7z2KuU5UTxI'
access_secret = 'g50MUUtL2bNQfZMhQr5WWOybzPFdD9jfF5gAKucPXzmj4'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

