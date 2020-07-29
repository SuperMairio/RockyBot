import os
import random
import discord
from discord.ext import commands
from topsecretfile.py import *

rockyBot = commands.Bot(command_prefix = "/") #Character to prefix commands so it knows im giving it a command

msgList = [
    "Im sad",
    "I miss Rocky",
    "Im stressed"
]
replyList = [
    "Don't be sad heres another photo!",
    "Hope this helps!",
    "Don't fur-get to take breaks!",
    "Rocky is proud of you, keep going!"
]

@rockyBot.event
def on_ready():
    print("RockyBot is online!")

def on_message(message):
    if message.content in msgList:
        reply = random.choice(replyList)     
        await message.channel.send(reply)
    # Send cat photo here

rockyBot.run(TOKEN)