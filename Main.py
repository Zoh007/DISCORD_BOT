import datetime
import time
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)
Token = input("What is your token? ")
print("Token is: " + Token + "\n")

## This is the indicator that the bot is online
@bot.event
async def on_ready():
  print("online", bot.user.name)

## Only uncomment the following code if have a server and if you know your channel id's

## You have to type in hi in the channel for the Welcoming members function to work....
# @bot.command()
# async def hi(ctx):
#   channel_id = (Input your channel id here)  ## This is a command for welcoming new members
#   if ctx.channel.id == channel_id:
#     author_name = ctx.author.name
#     await ctx.channel.send(
#       'This is the designated channel for welcoming new members!')
#     await ctx.send("Hi " + author_name)

## Use the following format: testmessage @XXXXXX "THE MESSAGE YOU WANT TO SEND"(While sending the message, don't use double quotes)
# @bot.command()
# async def testmessage(ctx, user_mention, *, message): 
#   if ctx.channel.id == (Input your channel id here) : This is a command for sending messages to members
#     user_send = ctx.message.mentions[0]
#     await user_send.send("Message: " + message + " from " + ctx.author.name)
#   else:
#     None  
  
## Type in hi in the channel to make the current date and time work
# @bot.command()
# async def currenttime(ctx):
#   if ctx.channel.id == 1199682638668107877:
#     current_date = datetime.datetime.now()
#     current_time = datetime.datetime.now().time()
#     formatted_date = current_date.strftime('%m-%d-%Y')
#     formatted_time = current_time.strftime('%I:%M:%S %p')
#     await ctx.channel.send(formatted_date)
#     await ctx.channel.send(formatted_time)

bot.run(Token)