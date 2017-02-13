import tweepy, time, sys, os, random
 
consumer_key = 'wvwesfGCFC1yBYLeoTD5fHjo5'
consumer_sercret = 'hqSQs71Ql9FiImnDcQsg9VK01gkm2DrwmZfeJmf8L8KzgcgaM9'

access_token = '819007392754974721-Mds0pbahkCBNziJ9NqPF4nLjlM7TtSe'
access_secret = 'iiF3NLlRgbjnwnXTpa4wmZxzz1eP29AR6JOrUB45Orr8x'

auth = tweepy.OAuthHandler(consumer_key, consumer_sercret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

media_list = []
for dirpath, dirnames, files in os.walk('Images'):
    for f in files:
    	media_list.append(os.path.join(dirpath, f))
media = random.choice(media_list)
str = 'Pictures?'
api.update_with_media(media, str)
time.sleep(15) # Sleep for 15 seconds

