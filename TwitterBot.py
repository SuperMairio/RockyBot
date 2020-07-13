import os
import sqlite3
import shutil
# This contains my API variables, make sure to insert your own
from topsecretfile import *
from twython import Twython, TwythonError

twitter = Twython(KEY, SECRET)
# Make sure you create the database using DatabaseManagment.py first
conn = sqlite3.connect('Usernames.db')

def Get_Image(): 
    try:
        photos = os.listdir(PHOTO_PATH):
    except(SystemError): #TODO: Check this is the only error
        photos = os.listdir(USED_PHOTO_PATH)
    
    photo = photos[0]
    return(photo)

def Send_Image():
    image = Get_Image()
    getUsernames = Get_Usernames()
    recipients = getUsernames[0]
    privleges = getUsernames[1] #TODO: Create functionality

    for(user in recipients):
        message = twitter.send_direct_message(screen_name=user,media=image)

    shutil.move(image, USED_PHOTO_PATH)

def Get_Usernames():
    unamesArray = [[],[]]
    cursor = conn.execute("SELECT NAME FROM Usernames;")
    cursor2 = conn.execute("SELECT ADMIN FROM Usernames;")

    for(row in cursor):
        unamesArray[0].append(row)
    
    for(row2 in cursor2):
        unamesArray[1].append(row2)

    return unamesArray

if(KEY == 'abc'):
    print("It looks like you haven't set your API keys\nYou can get them from: https://developer.twitter.com/en/apps")
else:
    Send_Image()

conn.close()
exit()
