import requests
import base64
import json
import pprint
import pandas as pd
import datetime

#### Step 1: # Obtaining StubHub User Access Token ####

## Enter user's API key, secret, and Stubhub login
app_token = input('Enter app token: ')
consumer_key = 'tumK1ova7330R7Dh8UfQe0a9LoWorPPY'
consumer_secret = 'bgImsM1IGuZWacvX'
stubhub_username = 'lchau91@gmail.com'
stubhub_password = '5m*8R0WgjQ*y'

## Generating basic authorization token
combo = consumer_key + ':' + consumer_secret
basic_authorization_token = base64.b64encode(combo.encode('utf-8'))
# print(basic_authorization_token)

## POST parameters for API call
headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic '+basic_authorization_token.decode('utf-8'),}
body = {
        'grant_type':'password',
        'username':stubhub_username,
        'password':stubhub_password,
        'scope':'PRODUCTION'}
## Making the call
url = 'https://api.stubhub.com/login'
r = requests.post(url, headers=headers, data=body)
token_response = r.json()
access_token = token_response['access_token']
user_GUID = r.headers['X-StubHub-User-GUID']