import os
import sqlite3
import shutil
# This contains my API variables, make sure to insert your own
from topsecretfile import *
from twython import Twython, TwythonError

twitter = Twython(KEY, SECRET)
conn = sqlite3.connect('Usernames.db')

def Get_Image(): 
    try:
        for photo in os.listdir(PHOTO_PATH):
    except(SystemError): #TODO: Check this is the only error
        for photo in os.listdir(USED_PHOTO_PATH)

    return(photo)

def Send_Image():
    image = Get_Image()
    recipients = Get_Usernames()
    response = twitter.upload_media(media=image ,media_type='image/jpeg', media_category='dmImage')
    
    shutil.move(image, USED_PHOTO_PATH)

def Get_Usernames():
    unamesArray = []
    cursor = conn.execute("SELECT NAME FROM Username;")
    for(row in cursor):
        unamesArray.append(row)
    
    return unamesArray

if(KEY == 'abc'):
    print("It looks like you haven't set your API keys\nYou can get them from: https://developer.twitter.com/en/apps")
else:
    Send_Image()

conn.close()
exit()