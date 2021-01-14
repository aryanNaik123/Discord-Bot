import discord 
import os 
import requests
import json 
import random 
import time 
import asyncio
import aiohttp
import urllib
from keep_alive import keep_alive

client = discord.Client()

sad_words = ['sad','depressed','unhappy','angry', 'miserable','depressing','annoying']

starter_encouragements = [
  'Cheer up!',
  'Hang in there', 
  "Atleast you're not a bot like me"
]
social_arr = ['twitter.com','youtube.com']

def get_quote(): 
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote

def dog_api(): 
  reponse = requests.get('https://dog.ceo/api/breeds/image/random')
  url = reponse.json()['message']
  urllib.request.urlretrieve(url, "sample.jpg")


@client.event 
async def on_ready(): 
  print('Logged in as {0.user}'.format(client))

@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return 
  msg = message.content
  if message.content.startswith('$dog'):
    dog = dog_api()
    await message.channel.send(file=discord.File('sample.jpg'))
  if message.content.startswith('$inspire'): 
    quote = get_quote() 
    await message.channel.send(quote)
  if any(word in msg for word in sad_words): 
    await message.channel.send(random.choice(starter_encouragements))
  if (str(msg) == 'lol'): 
    await message.channel.send('stop saying lol')
  if message.content.startswith('shark pog'):
    await message.channel.send(file=discord.File('tenor.gif'))
  if any(word in msg for word in social_arr):
    await message.channel.send('dont care')
  if message.content.startswith('$thumb'):
      channel = message.channel
      await channel.send('Send me that 👍 reaction, mate')

      def check(reaction, user):
          return user == message.author and str(reaction.emoji) == '👍'

      try:
          reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
          await channel.send('👎')
      else:
          await channel.send('👍')
keep_alive()

client.run(os.getenv('TOKEN'))