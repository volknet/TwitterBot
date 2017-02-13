import tweepy, time, sys, re, string, subprocess, os, random

from random import randint
consumer_key = 'wvwesfGCFC1yBYLeoTD5fHjo5'
consumer_sercret = 'hqSQs71Ql9FiImnDcQsg9VK01gkm2DrwmZfeJmf8L8KzgcgaM9'

access_token = '819007392754974721-Mds0pbahkCBNziJ9NqPF4nLjlM7TtSe'
access_secret = 'iiF3NLlRgbjnwnXTpa4wmZxzz1eP29AR6JOrUB45Orr8x'

auth = tweepy.OAuthHandler(consumer_key, consumer_sercret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def checkEnglishChar(str):
	try:
		str.encode('ascii')
	except UnicodeEncodeError:
		return False
	else:
		return True

mediaList = []
for dirpath, dirnames, files in os.walk('/Users/James/Desktop/Images'):
	for f in files:
		mediaList.append(os.path.join(dirpath, f))
media = random.choice(mediaList)

filename = open('tweet.txt','r')
tweettext = filename.readlines() 
filename.close()

for line in tweettext:
    finalList = []
    trends = api.trends_place(1)
    hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]

for i in range(len(hashtags)):
	if checkEnglishChar(hashtags[i]):
		finalList.append(hashtags[i])
	else:
		pass

x = randint(0, len(finalList))
print(finalList[x])

tweet = [s.replace('.', '') for s in tweettext]
tweetz = ''.join(tweet)
api.update_status(tweetz + '. ' + hashtags[x])


imageChoice = input('Attach a image?: ')
if imageChoice == 'Yes' or 'Y':
	api.update_with_media(media)
else:
	pass

print('Success...posted: ' + str(tweetz) + str(hashtags[x]) + str(mediaList))


