#import os library - access the environmental variable 
import os

#discord.py library 
import discord
#commands module with the discord.ext global context -define ways to interact with bot
from discord.ext import commands

#fetch TOKEN environmental variable, assign to token variable
token = os.getenv('TOKEN')

#creates bot object, wraps Discord connection
#command_prefix argument - defines how the bot identifies commands that it needs to handle
bot = commands.Bot(command_prefix="$")


#python decorator - lets us modify an object after its called
#registering an event callback - bot listens for events, function after decorator will be called whenever there's a message event from the server
@bot.listen()
#asynchronous function definition, passing Message object
async def on_message(message):
  #checks whether the message was sent by the bot user
  if message.author == bot.user:
    return

  #sends a message to the same channel that the message 
  await message.channel.send("Hello world!")  

#Log bot connection to console
@bot.listen()
async def on_ready():
  #fancy format for printing a string
  print(f'Connect to Discord as {bot.user}!')

bot.run(token)