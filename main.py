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
import socket
import telnetlib

# Minecraft Server Credentials
ip_env = str(os.getenv('ip'))
host_env = str(os.getenv('host'))


def isOpen(ip,port):
  a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  location = (ip, int(port))
  result_of_check = a_socket.connect_ex(location)

  if result_of_check == 0:
    return("Port is open")
  else:
    return("Port is not open")

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
  reponse = requests.get('https://dog.ceo/api/breed/corgi/images/random')
  url = reponse.json()['message']
  urllib.request.urlretrieve(url, "sample.jpg")

def mcsrv_api(): 
  ip = ip_env + ':' + host_env
  url = "https://api.mcsrvstat.us/2/" + ip
  raw = requests.get(url)
  return(raw.json()['players'])


@client.event 
async def on_ready(): 
  print('Logged in as {0.user}'.format(client))

@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return 
  msg = message.content
  if message.content.startswith('$corgi'):
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
  if message.content.startswith('$server'):
    await message.channel.send(isOpen(ip_env + ':' + host_env))
  if message.content.startswith('$ip'):
    await message.channel.send(ip_env + ':' + host_env)
  if message.content.startswith('$p'): 
    await message.channel.send(mcsrv_api())
keep_alive()

client.run(os.getenv('TOKEN'))