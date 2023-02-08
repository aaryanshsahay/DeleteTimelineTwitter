import yaml
from yaml.loader import SafeLoader
import tweepy
import datetime

from datetime import timedelta

import argparse



def initializeEnvironment(file_path):
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
	try:
		api.destroy_status(status_id)
	except:
		raise Exception(f"Could not delete tweet. Link : https://twitter.com/twitter/statuses/{status_id}")	from None


def DeleteTweetsCount(api, count = None):
	try:	
	
		num = 0
		for tweet in tweepy.Cursor(api.user_timeline).items():
				DeleteSingleTweet(status_id = tweet.id)
				num+=1

				if num == count:
					break

		print(f"Last {count} tweets deleted succesfully!")

	except: raise Exception("Count value should be a positive integer.") 


def DeleteTweetsSince(api, days = None):
	try:
		
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline, since_id = str(datetime.date.today() - timedelta(days = days))).items():
			DeleteSingleTweet(status_id = tweet.id)
			count+=1

		print(f"All tweets from {str(datetime.date.today() - timedelta(days = days))} till {str(datetime.date.today())} deleted succesfully.")
		print(f"Total tweets deleted : {count}")

	except: raise Exception("Error : Enter appopriate number of days to trace back from today.") from None


def DeleteAllTweets(api):
	try:
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

