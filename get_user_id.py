import tweepy

client = tweepy.Client(
    bearer_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
    consumer_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
    access_token='XXXXXXXXXXXXXXXXXXX', 
    access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
)

# Fetch your user ID write your @username
user_info = client.get_user(username='XXXXXXXXXXXXXXXXX')
print(f"Your user ID is: {user_info.data.id}")
