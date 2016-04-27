import tweepy

auth = tweepy.OAuthHandler('', '')

auth.secure=True
authUrl = auth.get_authorization_url()

#go to this url
print "Please Visit This link and authorize the app ==> " + authUrl
print "Enter The Authorization PIN"

#writing access tokes to file
pin = raw_input().strip()
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens","w")
accessTokenFile.write(token[0]+'\n')
accessTokenFile.write(token[1]+'\n')
