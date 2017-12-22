class authentication:

    def __init__(self):
        # Go to http://apps.twitter.com and create an app.
		# The consumer key and secret will be generated for you after
        self.consumer_key ="fWU3vQKFwe1vpBlHd62g99CzI"
        self.consumer_secret="CdgpTr0oCI0VyutUMqjyKORyerTokKcPfl242KJxcUSet3Zhf8"

        # After the step above, you will be redirected to your app's page.
        # Create an access token under the the "Your access token" section
        self.access_token="1675555622-Fl4NaSWRpcqYGC0HL9g1ZU3YgikPWGWv45sSp57"
        self.access_token_secret="VFU1Hu5xDaNaKLqcflokbXY7GIgDU0D5x4xhZjJyJAHKQ"

    def getconsumer_key(self):
            return self.consumer_key
    def getconsumer_secret(self):
            return self.consumer_secret
    def getaccess_token(self):
            return self.access_token
    def getaccess_token_secret(self):
            return self.access_token_secret