import tweepy, re

consumer_key = 'wvwesfGCFC1yBYLeoTD5fHjo5'
consumer_sercret = 'hqSQs71Ql9FiImnDcQsg9VK01gkm2DrwmZfeJmf8L8KzgcgaM9'

access_token = '819007392754974721-Mds0pbahkCBNziJ9NqPF4nLjlM7TtSe'
access_secret = 'iiF3NLlRgbjnwnXTpa4wmZxzz1eP29AR6JOrUB45Orr8x'

auth = tweepy.OAuthHandler(consumer_key, consumer_sercret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

file_handler = open('putfile.txt', 'w')
grab = []

search = api.search(q='Python', count = 1)

startContent = 'text: '
endContent = 'truncated:'

for line in search:
	test = re.search('test:', str(line))
print(test)

