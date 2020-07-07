import os
# This contains my API variables, feel free to insert your own
from topsecretfile import *
from twython import Twython, TwythonError

if KEY == 'abc':
    print("It looks like you haven't set your API keys\nYou can get them from: https://developer.twitter.com/en/apps")

twitter = Twython(KEY, SECRET)

#send_direct_message

def GetNextImage():
    for photo in os.listdir(PHOTO_PATH):
        return(photo)