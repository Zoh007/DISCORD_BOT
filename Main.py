import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)
Token = input("What is your token? ")
print("Token is: " + Token + "\n")

@bot.event
async def on_ready():
  print("online", bot.user.name)

# Only uncomment the following code if know your channel id's
# @bot.command()
# async def hi(ctx):
#   channel_id = input("What is your channel id? ")
#   if ctx.channel.id == channel_id:
#     author_name = ctx.author.name
#     await ctx.channel.send(
#       'This is the designated channel for welcoming new members!')
#     await ctx.send("Hi " + author_name)


# @bot.command()
# async def testmessage(ctx, user_mention, *, message):
#   if ctx.channel.id ==:
#     user_send = ctx.message.mentions[0]
#     await user_send.send("Message: " + message + " from " + ctx.author.name)
#   else:
#     None


bot.run(Token)