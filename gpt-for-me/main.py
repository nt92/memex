import tweepy
import csv

# Replace these with your own Twitter API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_all_likes(api):
    likes = []
    for status in tweepy.Cursor(api.favorites).items():
        tweet = {
            'id': status.id_str,
            'created_at': status.created_at,
            'text': status.text,
            'user': status.user.screen_name,
        }
        likes.append(tweet)
    return likes


def save_likes_to_csv(likes, filename='likes.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'created_at', 'text', 'user']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for like in likes:
            writer.writerow(like)


if __name__ == "__main__":
    likes = get_all_likes(api)
    save_likes_to_csv(likes)
