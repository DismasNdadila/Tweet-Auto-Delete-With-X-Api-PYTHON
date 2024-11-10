import time
import tweepy

client = tweepy.Client(
    bearer_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 
    consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx', 
    consumer_secret='xxxxxxxxxxxxxxxxxxxxxxx', 
    access_token='xxxxxxxxxxxxxxxxxxxxxxxxxx', 
    access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

# User ID of the account whose tweets you want to delete run the get_user_id.py script to get the user ID
user_id = 'xxxxxxxxxxxxxxxxxxxxxxxx'


def fetch_and_delete_tweets(user_id):
    next_token = None  

    while True:
        try:

            tweets_response = client.get_users_tweets(id=user_id, max_results=100, pagination_token=next_token)

            if 'data' not in tweets_response:
                print("No more tweets to delete.")
                break

            for tweet in tweets_response.data:
                try:
                    client.delete_tweet(tweet.id)
                    print(f'Deleted tweet ID: {tweet.id}')
                except Exception as e:
                    print(f'Failed to delete tweet ID {tweet.id}: {e}')

            next_token = tweets_response.meta.get('next_token', None)
            if not next_token:
                print("No more pages of tweets.")
                break  

        except tweepy.errors.TooManyRequests as e:
            print("Rate limit exceeded. Waiting for 15 minutes...")
            time.sleep(15 * 60)  
        except Exception as e:
            print(f"An error occurred: {e}")
            break 

fetch_and_delete_tweets(user_id)

