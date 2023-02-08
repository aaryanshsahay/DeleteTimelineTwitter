# DeleteTimelineTwitter
## About
Recently discorvered that you can't delete all of your tweets in one go, rather have to delete them one by one like we're in 1846. Using this you can delete all tweets in one go (or 'n' number of tweets). This way you dont have to create a new twitter handle for every new personality you develop.

With the help of this you can :
1. Delete 'n' tweets.
2. Delete all historical tweets 'n' days from today.
3. Delete all tweets in your timeline*.

*Note - Tweepy has a constraint and can only delete a maximum of 3000 tweets in a single run. If you want to delete more, you can run the script multiple times until its completely cleared. 


### <b>You need to signup for a developer account (to get the keys & tokens) for the script to work.</b>


## Contents: 

1. [How to get keys & tokens](#keysandtokens)
2. [Running Directly](#startup) 
3. [example](#example)  

<a name="keysandtokens"/>

## How to get the keys & tokens

1. Apply for a developer account (dont have to create a new acccount, just have to complete a quick survey and its done.). Follow the first 5 steps on this [link](https://developer.twitter.com/en/support/twitter-api/developer-account).

2. Get your api keys (api & secret) & access (access & secret) from here.
![image](https://user-images.githubusercontent.com/53135035/217559020-db0b0ece-e73f-47f6-b32d-c2ac2a6013e8.png)

For further [reference](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret).




<a name = "startup"/>

## Running it directly



After cloning the repository, add your api keys to the config.yaml file and then
run : ` pip install -r requirements.txt`
then run this command :
`python main.py -h`

the output will be :
```
usage: RestartTwitterTimeline [-h] [--count COUNT] [--days DAYS] [--all ALL]

Deletes tweets made from your account. Can delete : 1) Last 'n' tweets. 2) Tweets made between today and 'n' days ago. 3) All tweets (max limit is 3000)

optional arguments:
  -h, --help     show this help message and exit
  --count COUNT  The number of tweets to be deleted (should be a positive integer)
  --days DAYS    Delete tweets from previous days.
  --all ALL      Delete all tweets, pass 'True'.
```
The arguments are :
1. `--count` the number of tweets need to be deleted.
2. `--days` delete all tweets made between today and 'n' days ago.
3. `--all` delete all tweets (limit is 3000 -> tweepy constraint).

Since the max tweets which can be deleted at any moment is 3000, if you wish to delete more than that, run the script multiple times.

*could also script this xD*




<a name = "example"/>

## Example

On running `python main.py --count 10` , the output is : `Last 10 tweets deleted succesfully!`. Verifying with my personal twitter handle, the tweets were successfully deleted.


