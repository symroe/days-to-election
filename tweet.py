from datetime import date

from twitter import Twitter
from twitter.oauth import OAuth

from settings import *

if not all([OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET]):
    raise "Not configured.  Populate settings.py"

t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

d1 = date.today()
d2 = date(2015, 05, 07)
delta = d2 - d1

t.statuses.update(
    status="Only %s days until the 2015 General Election!" % delta.days)