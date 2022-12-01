import discord
from discord.ext import commands
import os
from replit import db
from textblob import TextBlob

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents = intents)
client = discord.Client(prefix='', intents = intents)

@client.event
async def on_message(message):
  if message.author.id == 323671262708760576:
    wordlist = message.content.split(" ")
    reconstructedmessage = ""
    cleanmessage = ""
    for word in wordlist:
      reconstructedmessage = reconstructedmessage + " " + word.lower()
      cleanword = str(TextBlob(word.lower()).correct())
      cleanmessage = cleanmessage + " " + cleanword
    if reconstructedmessage != cleanmessage:
      await message.channel.send(f"{message.author.mention} Avery you fucked up. You should've said something like: \n\n" + cleanmessage)
  #This is the amend ffunction, it doesn't work rn
  #if message.content.startswith("$amend"):

print("Booted up")

client.run(os.environ['privateid'])
