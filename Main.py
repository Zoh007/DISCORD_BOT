from datetime import datetime
from pytz import timezone 
import pytz
import discord
from discord.ext import commands
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)
Token = input("What is your token? ")
print("Token is: " + Token + "\n")

## This is the indicator that the bot is online
@bot.event
async def on_ready():
  print("online", bot.user.name)

## Only uncomment the following code if have a server and if you know your channel id's

# You have to type in hi in the channel for the Welcoming members function to work....
@bot.command()
async def hi(ctx):
  channel_id = 1201563193047253113 ## This is a command for welcoming new members
  if ctx.channel.id == channel_id:
    author_name = ctx.author.name
    await ctx.channel.send(
      'This is the designated channel for welcoming new members!')
    await ctx.send("Hi " + author_name)

## Use the following format: testmessage @XXXXXX "THE MESSAGE YOU WANT TO SEND"(While sending the message, don't use double quotes)
# @bot.command()
# async def testmessage(ctx, user_mention, *, message): 
#   if ctx.channel.id == (Input your channel id here) ## This is a command for sending messages to members
#     user_send = ctx.message.mentions[0]
#     await user_send.send("Message: " + message + " from " + ctx.author.name)
#   else:
#     None  
  
## Type in currenttime and then after a space, write the specified time zone you want.
# @bot.command()
# async def currenttime(ctx, message):
#   if ctx.channel.id == #(Input the channed id):  ## This is a command for knowing the current date and time:
#     timezone = pytz.timezone(message)
#     current_date = datetime.datetime.now(timezone)
#     current_time = datetime.datetime.now(timezone)
#     formatted_date = current_date.strftime('%m-%d-%Y')
#     formatted_time = current_time.strftime('%I:%M:%S %p')
#     await ctx.channel.send(formatted_date)
#     await ctx.channel.send(formatted_time)
  
# Used to remember important dates
# @bot.command()
# async def rememberdate(ctx, message1, message2):
#   if ctx.channel.id == 1200478885675016293:  ## This is a command for knowing the current date and time:
#     current_date = datetime.now()
#     input_date = datetime.strptime(message2,'%m-%d-%Y')
#     if current_date.date() == input_date.date():
#       await ctx.channel.send("The date for " + message1 + " is today.")
  
@bot.command()
async def gameplay(ctx):
  if ctx.channel.id == 1202946047027056710:
    await ctx.channel.send('Do you want to play a game?')
    button = discord.Button(style=discord.ButtonStyle.blue, label="Click me!")

    message = await ctx.send("Press the button:", components=[button])

    # Wait for the button to be clicked
    interaction = await bot.wait_for("button_click", check=lambda i: i.component.label.startswith("Click me!"))

    # Respond to the button click
    await interaction.respond(content="Button clicked!")

bot.run(Token)