#!/usr/bin/env python
import sys
from twython import Twython
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

page = 'http://eng.koreabaseball.com/Standings/TeamStandings.aspx'
_page = urlopen(page)
soup = BeautifulSoup(_page, 'html.parser')
#print(type(soup))

#box = soup.find('td', attrs = {'title':'TEAM'})
#print(box.text.encode('utf-8').decode("utf-8").strip())

#box2 = soup.find('td', title='PK')
#print(box2.text.encode('utf-8').decode("utf-8").strip())

#a = soup.title
#a = soup.get_text()
a = soup.find_all('td', title='TEAM')
#print(a[:10])

rank = []
for i in a[:10]:
    rank.append(i.text)
#    print(i.text)
#print(rank)

### convert list to string
def ToString(l):
    str1 = ""
    lst = [1,2,3,4,5,6,7,8,9,10]
    b = 1
    for i in l:
        str1 += str(b) +": "+  i+ "\n"
        b += 1
    return str1

#print(ToString(rank))

now = datetime.now(timezone('Asia/Seoul'))
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print(date_time)

### twitter consumer and access information
apiKey = 'gF9e5F4n3Cu76r6TZjIfUr4kN'
apiSecret = 'o0yKzmxoZNikvN4BGFmvrBgR3Fivf9Muc4GHxyieTCfj2kdzhx'
accessToken = '1269599871012442115-Up5QpjmTW2VbWJ2n0n31f5fXmH32Jw'
accessTokenSecret = 'qgaWdmsjliWS4wGQD6BrYhlh3ByU11Jgf14uhExmcdfAW'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

### emoji converted from bytes to string
emo = b'\xF0\x9F\x92\x99'
emo2 = b'\xE2\x9A\xBE'
_emo2 = emo2.decode('utf-8')
_emo = emo.decode('utf-8')

### tweeting on the twitter page
api.update_status(status= _emo + ' Korean Baseball Ranking for today! ('+date_time+')'+_emo+'\n\n'+ ToString(rank)+'\n\nCheer up for your team! '+_emo2)

print("Tweeted!")
