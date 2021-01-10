import discord 
import os 
import requests
import json 
import random 

client = discord.Client()

sad_words = ['sad','depressed','unhappy','angry', 'miserable','depressing','annoying']

starter_encouragements = [
  'Cheer up!',
  'Hang in there', 
  "Atleast you're not a bot like me"
]

def get_quote(): 
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote

@client.event 
async def on_ready(): 
  print('Logged in as {0.user}'.format(client))

@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return 
  
  if message.content.startswith('$hello'): 
    await message.channel.send('hello!')

@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return 

  msg = message.content

  if message.content.startswith('$inspire'): 
    quote = get_quote() 
    await message.channel.send(quote)
  if any(word in msg for word in sad_words): 
    await message.channel.send(random.choice(starter_encouragements))
  if (str(msg) == 'lol'): 
    await message.channel.send('stop saying lol')

@client.event
  if message.content.startswith('what','why'):
    
client.run(os.getenv('TOKEN'))
