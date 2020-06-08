#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Hello, this page is for OSS class made by Soo Min Lee!"

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'gF9e5F4n3Cu76r6TZjIfUr4kN'
apiSecret = 'o0yKzmxoZNikvN4BGFmvrBgR3Fivf9Muc4GHxyieTCfj2kdzhx'
accessToken = '1269599871012442115-Up5QpjmTW2VbWJ2n0n31f5fXmH32Jw'
accessTokenSecret = 'qgaWdmsjliWS4wGQD6BrYhlh3ByU11Jgf14uhExmcdfAW'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
