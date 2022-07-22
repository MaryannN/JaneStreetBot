#import os library - access the environmental variable 
import os

#commands module with the discord.ext global context -define ways to interact with bot
from discord.ext import commands

#import request libray to send requests to quotes API
import requests

#import json library for parsing json data
import json

#so we can pick a random quote
import random

#for the yoda thingy
import yoda

#fetch TOKEN environmental variable, assign to token variable
token = os.getenv('TOKEN')

#creates bot object, wraps Discord connection
#command_prefix argument - defines how the bot identifies commands that it needs to handle
bot = commands.Bot(command_prefix="$")

'''
Greeting
'''

#python decorator - lets us modify an object after its called
#registering an event callback - bot listens for events, function after decorator will be called whenever there's a message event from the server
@bot.listen()
#asynchronous function definition, passing Message object
async def on_message(message):
  #checks whether the message was sent by the bot user
  if message.author == bot.user:
    return

  #code so bot only greets when you greet it specifically 
  if message.content == "Hello MaryannBot!":
  
  #sends a message to the same channel that the message 
    await message.channel.send("Hello world!")  


#Log bot connection to console
@bot.listen()
async def on_ready():
  #fancy format for printing a string
  print(f'Connect to Discord as {bot.user}!')



'''
Echo Command
'''

#adding documentation to the help command, can call echo cammand with $e
@bot.command(name= "e", help="Echoes provided text back to the channel")
#ctx is a Context object - context in which the command was invoked
#arg - additional argument 
#asterisk lets us capture a varible number of arguments - captures tokens in the message aka echos whole message

async def echo(ctx, *arg):
  #arg is now a tuple of tokens so it has to be glued back together
  await ctx.send(" ".join(arg))


'''
Inspirational Quotes
'''
#Using zenquotes.io API

def get_quotes():
  #makes HTTP request to the quote endpoint - asking website to give us some data using a specific protocol that the website knows how to respond to
  #response - Response object containing the data from zenquotes.io + some server metadata
  response = requests.get("https://zenquotes.io/api/quotes")
  #load text into json format, quotes variable is a list of python dictionaries 
  quotes = json.loads(response.text)
  return quotes

quotes = get_quotes()

def get_quote():
  quote = random.choice(quotes)
  #formatting - backslashes so string doesn't end, 
  quote = f"{quote['a']} said, \"{quote['q']}\""
  return(quote)


@bot.command(name="inspire", help="Send an inspirational quote to the channel")
async def inspire(ctx, *args):
  await ctx.send(get_quote())

#note so self - maybe find a way to add my fav quotes, reflectly?

'''
Yoda
'''
#https://github.com/haohangxu/yoda-translator 

def get_yodaquote():
  quote = random.choice(quotes)
  yodaquote = yoda.translate(quote['q'])
  quote = f"Yoda-{quote['a']} said, \"{yodaquote}\""
  return(quote)

@bot.command(name="yoda", help="Send yoda-fied quote")

async def inspire(ctx, *args):
  await ctx.send(get_yodaquote())

'''
Closing
'''
bot.run(token)