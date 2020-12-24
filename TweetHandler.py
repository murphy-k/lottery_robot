import tweepy


class TweetHandler:
    def __init__(self, status):
        # API keys
        self.consumer_key = "vSCGwcRey2yn8d17D2mQ7aDpc"
        self.consumer_secret = "gSZy4rPkinRIZhGwzuwBxgIlzjK4wBqQYyR0GXjyvpnzMTtX35"
        self.access_token = "1253898917143592960-Rc0Mlos6BX4palcP47yNVJwDsrtiGI"
        self.access_token_secret = "gzgIVTBubEyvf18kKR6n7t05gFecspTYmlMSu0uvgaIrs"

        # authentication of consumer key and secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)

        # authentication of access token and secret
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(self.auth)

        # update the status
        api.update_status(status=str(status))


test = TweetHandler("Testing!")
