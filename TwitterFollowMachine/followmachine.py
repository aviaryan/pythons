import tweepy
from collections import deque

# CONFIG
# max number of accounts to follow
limit = 100
# the base users whose followers will be followed
userstart = ['MozillaIN', 'googleindia', 'twitter']

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

## END OF CONFIG SECTION
###################################################

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


# timeline = api.user_timeline()
# # dir vars inspect
# for i in timeline:
# 	print( dir(i) )

heyme = api.me()
print('Signed in as', heyme.name)
following = set( api.friends_ids( heyme.id ) )
print( 'currently following', len(following) )

q = deque()
for i in userstart:
	user = api.get_user(i)
	q.append(user.id)

# generate the to-follow list
while len(q) > 0 and limit > 0:
	root_following = api.followers_ids( q[0] )
	print('taking root id', q[0], ', followers count', len(root_following))
	for i in root_following:
		if i not in following:
			q.append(i)
	if q[0] not in following:
		try:
			root = api.create_friendship( q[0] )
			following.add(q[0])
			print('followed', q[0])
			limit -= 1
		except Exception as e:
			print('error following', q[0], e)
	q.popleft()

	if len(q) > limit: # enough people dont waste api calls
		break

# follow the people
while len(q) > 0 and limit > 0:
	try:
		root = api.create_friendship( q[0] )
		print('followed', q[0])
	except Exception as e:
		print('error following', q[0], e)
	q.popleft()
