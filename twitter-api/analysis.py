# analysis.py

import simplejson as json

with open('sample.json') as f:
  tweets = json.load(f)

print tweets.keys()

import pandas as pd

def user_screen_name(user):
  return user['screen_name']

df_tweets = pd.DataFrame(data=tweets['statuses'])
df_tweets = df_tweets.sort_values(by='retweet_count', ascending=False)
df_tweets['user_screen_name'] = df_tweets['user'].apply(user_screen_name)
df_tweets.to_csv('sample_refined_sorted.csv', encoding='utf-8')

# df_tweets.to_csv('sample.csv', encoding='utf-8')


# df_tweets.to_csv('sample_refined.csv', encoding='utf-8')

# print df_tweets.head()
# print df_tweets.user



# df_tweets['text'] = map(lambda tweet: tweet['text'], tweets)
