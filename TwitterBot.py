import os
# This contains my API variables, make sure to insert your own
from topsecretfile import *
from twython import Twython, TwythonError
import sqlite3
import shutil

if KEY == 'abc':
    print("It looks like you haven't set your API keys\nYou can get them from: https://developer.twitter.com/en/apps")
    exit()

twitter = Twython(KEY, SECRET)

#send_direct_message

def Get_Image(): 
    try:
        for photo in os.listdir(PHOTO_PATH):
    except(SystemError):
        for photo in os.listdir(USED_PHOTO_PATH)

    return(photo)

def Send_Image():
    image = Get_Image()

    response = twitter.upload_media(media=image ,media_type='image/jpeg', media_category='dmImage')

    shutil.move(image, USED_PHOTO_PATH)
    
def Get_Usernames():
    # sqlite code here

Send_Image()
exit()