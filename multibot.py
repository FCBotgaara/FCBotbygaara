import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import re
import time

bot = commands.Bot(command_prefix='#')


def refreshus(): #function to get data for us server
    source = requests.get('https://glaca.nostale.club/api/en/2/') #url for us server
    page = source.text
    x = re.split(r"\W+", page)

    angelpercent = x[9]
    devilpercent = x[20]
    updatetime = int(x[11])//1000
    currenttime = int(time.time())
    timeagosec = currenttime - updatetime
    timeh = timeagosec//3600
    timem = (timeagosec%3600)//60
    return(angelpercent, devilpercent, timeh, timem)

def refreshcz(): #funtion to get fc data for cz server
    source = requests.get('https://glaca.nostale.club/api/cz/1/') #url for cz server
    page = source.text
    x = re.split(r"\W+", page)

    angelpercent = x[9]
    devilpercent = x[20]
    updatetime = int(x[11])//1000
    currenttime = int(time.time())
    timeagosec = currenttime - updatetime
    timeh = timeagosec//3600
    timem = (timeagosec%3600)//60
    return(angelpercent, devilpercent, timeh, timem)

@bot.event
async def on_ready():
    print("Ready when you are")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def fcus(): #bot command for #fcus
    await bot.say("""Angel Percentage: %s
Devil Percentage: %s
Last update: %d hours %d minutes ago
Server: US""" % refreshus()) #this part calls variables from refreshus() function
    print("fc status posted for us")


@bot.command(pass_context=True)
async def fccz(): #bot command for #fccz
    await bot.say("""Angel Percentage: %s
Devil Percentage: %s
Last update: %d hours %d minutes ago
Server: CZ""" % refreshcz()) #this part calls variables from refreshcz() function
    print("fc status posted for cz")

bot.run("NDQ1MjYyNDc3NTM4NzU0NTkx.DfMItQ.PzZR-fxa2LjMP9Ob6u_bWghJw0g")
