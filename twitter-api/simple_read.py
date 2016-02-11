import simplejson as json

with open('keychain.json') as f:
  keychain = json.load(f)

print keychain.keys()

from requests_oauthlib import OAuth1

def get_oauth():
  oauth = OAuth1(keychain['CONSUMER_KEY'],
              client_secret=keychain['CONSUMER_SECRET'],
              resource_owner_key=keychain['OAUTH_TOKEN'],
              resource_owner_secret=keychain['OAUTH_TOKEN_SECRET'])
  return oauth

oauth = get_oauth()

import requests
# https://twitter.com/osulop/status/697391618492604416

# https://twitter.com/jnkka/status/696702852736090112

url = 'https://api.twitter.com/1.1/statuses/show.json?id=696702852736090112'
r = requests.get(url=url, auth=get_oauth())
print dir(r.json())
print type(r.json())
print r.json()['text']

# data = json.loads(r.json())

# print data

with open('example.json','w') as f:
  json.dump(r.json(),f,indent=1)

# print dir(r.json)

# 'https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi', )

















