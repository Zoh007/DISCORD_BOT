import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)
Token = input("What is your token?")


@bot.event
async def on_ready():
  print("online", bot.user.name)


@bot.command()
async def hi(ctx):
  if ctx.channel.id == 1087788515623977000:
    author_name = ctx.author.name
    await ctx.channel.send(
      'This is the designated channel for welcoming new members!')
    await ctx.send("Hi " + author_name)


@bot.command()
async def testmessage(ctx, user_mention, *, message):
  if ctx.channel.id == 1156608903832940674:
    user_send = ctx.message.mentions[0]
    await user_send.send("Message: " + message + " from " + ctx.author.name)
  else:
    None


bot.run(Token)