import os
import discord
import requests
import json
import random

client = discord.Client()

sad_words = ["sad","depressed" ,"depressing","mad", "miserable", "unhappy", "angry"  ]

starter_encouragements = ["Cheer up Bud","Almost there" ,"Youre a Winner"," Its understandable, we will get through this", "Its going to be alright" , " There is nothing that cannot be overcome"   ]

my_secret = os.environ['TOKEN'] 

def get_Quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

  
@client.event 
async def on_ready():
  print('logged in as {0.user}'.format(client) )

@client.event 
async def on_message(message):
  
  msg = message.content
  
  if message.author == client.user:
    return
  
  if message.content.startswith('hello'):
    await message.channel.send('Hello Bud How are you today ?')

  if "thanks" in message.content:
    await message.channel.send('Youre welcome')
  
  if "Thanks" in message.content:
    await message.channel.send('Youre welcome')
    
  if message.content.startswith('inspire'):
    quote = get_Quote()
    await message.channel.send(quote)
 

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(my_secret)
  
 

