#code to print tweets and emojis in python
import tweepy

consumer_key =	'XoEyCZV0B40QhvDnagGdvw8MV'
consumer_secret = 'GVLqJtr2OMaGDKe0BOU3r5Z28buvWW1Ry43uLXXsNglXQf7byR' 
access_token = '1014847920808648704-xeURjluOHHezJrRFzBPn10NRyDntTf'
access_token_secret = 'Tr3EVosi4EMKnQljPOejN5lCgSPTleH7slsexyDR08irR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API (auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text.encode("utf-8"))


#Join a list into a sentence
name = ["Joshua"] + ["is great"]
print (name)

def date():
    date = ('You want the date?')
    print (762018)

#this is the code to print out are and volume of a sphere    
import math
def radius():
    radius = int( input("radius"))
    Area = (math.pi * radius * radius)
    Volume = (2 * math.pi * radius)
    answers = {"Area" : Area, "Volume" : Volume}
    print (answers)

# code to get a user's age
def get_age():
    age = int( input("Tell me your age"))
    print(age)

#code to get a user's name
def get_name():
    name = str( input("Tell me your name"))
    print(name)

#code to call out user's name and age
def Joshua():
    name = {"Joshua Ampofo"}
    age = {26}
    Answer =  {"name" : name, "age" : age}
    print(Answer)

name = ['the']
word[0:1]

sentence = 'where\n are\n you'
print (sentence)
    

#global_code_files
