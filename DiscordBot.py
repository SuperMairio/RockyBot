import os
import random
import shutil
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORDTOKEN")
PHOTO_PATH = os.getenv("PHOTOPATH")
USED_PHOTO_PATH = os.getenv("USEDPHOTOPATH")
CHANNELID = os.getenv("CHANNELID")

rockyBot = commands.Bot(command_prefix = "/")
msgList = [
    "Im sad",
    "I miss Rocky",
    "Im stressed",
    "I want to see my boy",
    "Where is my son",
    "test"
]
replyList = [
    "Don't be sad heres another photo!",
    "Hope this helps!",
    "Rocky is proud of you, keep going!"
]

@rockyBot.event
async def on_ready():
    print("RockyBot is online!")

@rockyBot.event
async def on_message(message):
    photo = Get_Photo()

    if message.content in msgList:
        reply = random.choice(replyList)  
        await rockyBot.wait_until_ready()
        channel = rockyBot.get_channel(CHANNELID)  
        await message.channel.send(reply)
        await channel.send(file=discord.File((PHOTO_PATH+"/"+photo)))
    
    shutil.move(PHOTO_PATH+photo, USED_PHOTO_PATH)

def Get_Photo(): 
    try:
        photos = os.listdir(PHOTO_PATH)
    except(SystemError): #TODO: Check this is the only error
        photos = os.listdir(USED_PHOTO_PATH)
    
    photo = random.choice(photos)
    print(photo)
    return(photo)

rockyBot.run(TOKEN)