import tweepy
import json

#override tweepy.StreamListener to add logic to on_status and add tweet limits
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api, tweet_limit = 50):
        self.api = api
        self.tweet_limit = tweet_limit
        self.current_tweet_count = 0

    def on_status(self, status):
        txt = status.text

        # check to see if this is a retweet
        if txt.startswith('RT @'):
            pass
        # Check to see if there's a URL in there (URLs are not interesting on
        # images unless they're mine)
        elif 'http' in txt:
            pass
        # We also don't want mentions, so no @s:
        elif '@' in txt:
            pass
        else:
            try:
                # We don't want any tweets with non ascii characters in them.
                txt = txt.decode('ascii')
                tweet_dict = dict(user=status.user.name, tweet=txt)
                #user = status.user.name
                #tweet = txt
                with open('twitter_data', 'a') as f:
                    f.write(json.dumps(tweet_dict)) # TODO - put a new line after this
                    print tweet_dict
                self.current_tweet_count += 1
                if self.current_tweet_count >= self.tweet_limit:
                    exit()
            except: pass


auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

myStreamListener = MyStreamListener(tweet_limit=1, api=api)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
# print myStream.__dict__
myStream.filter(track=['twitter'], languages=['en'])

# Get an image



# Turn it into a meme
from PIL import Image, ImageFont, ImageDraw

img = Image.open('<IMG>')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf') # could put font size here to ensure it's the right size

draw.text((10,10), "<Tweet>", font=font)
draw.text((10,10), "- <Author>", font=font) # Put the Author in the lower left, italicized
img.save(fp='<path>', format='PNG')

# Tweet the image out
# Probably don't want to do this on *My* twitter page.
