"""
============================================================================


	100% Free of cost.

	Go thorugh the read me file first!!!
	There's a guide both on how to use this for both, people who
	dont know how to code as well as people who do know.

	Enjoy! 

    @AaryanshSahay February 2023.
	

============================================================================
"""


import yaml
from yaml.loader import SafeLoader
import tweepy
import datetime

from datetime import timedelta

import argparse



def initializeEnvironment(file_path):
	"""
	Reads the appropriate api keys and access tokens from the config.yaml file,
	initialzies the environment and sets the 'api' variable which will be used 
	later.

	Args :
		1) file_path (str) : relative path to the config.yaml file

	Returns : 
		1) tweepy api object

	"""
	try:
		with open(file_path) as f:
			data = yaml.load(f, Loader = SafeLoader)
			api_key, api_key_secret = data['api_key'], data['api_key_secret']
			access_token, access_token_secret = data['access_token'], data['access_token_secret']

			auth = tweepy.OAuthHandler(api_key, api_key_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth)

			return api

	except:
		raise Exception("Invalid or Expired API keys: The keys entered are either incorrect or have expired. If the same error persists after multiple attempts, regenerate the keys.") from None


def DeleteSingleTweet(status_id):
	"""
	Deletes a single tweet permanently. Does not return anything.
	api is not passed as an argument because this function will inherit from a parent function
	which already has the api argument initialized.

	Args : 
		1) status_id (str) : id of a tweet

	returns :
		None
	"""
	try:
		api.destroy_status(status_id)
	except:
		raise Exception(f"Could not delete tweet. Link : https://twitter.com/twitter/statuses/{status_id}")	from None


def DeleteTweetsCount(api, count = None):
	"""
	Deletes last 'n' tweets from the most recent tweet.

	Args : 
		1) api : tweepy api object
		2) count (int) : number of tweets to be deleted. Defaults to None.

	returns :
		None
	"""
	try:	
		print("="*25,"Deleting Tweets!!!!","="*25)
		num = 0
		for tweet in tweepy.Cursor(api.user_timeline).items():
				DeleteSingleTweet(status_id = tweet.id)
				num+=1

				if num == count:
					break

		print(f"Last {count} tweets deleted succesfully!")

	except: raise Exception("Count value should be a positive integer.") 


def DeleteTweetsSince(api, days = None):
	"""
	Deletes tweets from the last 'n' days from the day of running the script.

	Args :
		1) api : tweepy api object
		2) days (int) : the number of days, defaults to None.
	
	returns :
		None
	"""  
	try:
		print("="*25,"Deleting Tweets!!!!","="*25)
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline, since_id = str(datetime.date.today() - timedelta(days = days))).items():
			DeleteSingleTweet(status_id = tweet.id)
			count+=1

		print(f"All tweets from {str(datetime.date.today() - timedelta(days = days))} till {str(datetime.date.today())} deleted succesfully.")
		print(f"Total tweets deleted : {count}")

	except: raise Exception("Error : Enter appopriate number of days to trace back from today.") from None


def DeleteAllTweets(api):
	"""
	Deletes every single tweet in the user's timeline. The max limit is 3000. (tweepy limitation)
	
	Args : 
		1) api : tweepy api object

	returns : 
		None
	"""
	try:
		print("="*25,"Deleting Tweets!!!!","="*25)
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline).items():
			DeleteSingleTweet(status_id = tweet.id)
			count+=1

		
		print("All tweets successfully deleted!")
		print(f"Total tweets deleted : {count}")

	except: raise Exception("Error Occured") from None


if __name__ == "__main__":

	parser = argparse.ArgumentParser(
						prog = "RestartTwitterTimeline",
						description = """Deletes tweets made from your account. Can delete : \n1) Last 'n' tweets.\n2) Tweets made between today and 'n' days ago. \n3) All tweets (max limit is 3000)""",
						)

	parser.add_argument('--count',type = int, help = "The number of tweets to be deleted (should be a positive integer)")
	parser.add_argument('--days', type = int, help = "Delete tweets from previous days.")
	parser.add_argument('--all', type = bool, help = "Delete all tweets, pass 'True'.")

	args = parser.parse_args()

	count, days, _all = args.count, args.days, args.all

	file_path = "config.yaml"
	api = initializeEnvironment(file_path)

	if _all != None:
		DeleteAllTweets(api)

	elif days != None:
		DeleteTweetsSince(api, days = days)

	elif count!= None:
		DeleteTweetsCount(api, count = count)

