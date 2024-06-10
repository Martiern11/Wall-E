# writing the code bot #
# importing modules #
import discord 
import os 
import random 
from dotenv import load_dotenv 
from ec2_metadata import ec2_metadata 

print('This is my Ec2_metadata.region:', ec2_metadata.region)
print('This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initializing variables #
load_dotenv() 
 
# Creating instancec for the discord bot #

client = discord.Client(messages=True, guilds=True)
token = str(os.getenv('TOKEN')) #Creating client to send a request to disord API #

# Initializing the Bot #
@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client)) 

# Array of jokes for the bot to tell #
jokes_responses = {
    "Why do programmers prefer dark mode?" : "Because light attracts bugs!",
    "Why did the programmer quit his job?" : "Because he didn't get arrays"
}

# Setting appropiate response to user meassage #    
@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
  
    if channel == "general": 
        if user_message.lower() == "Hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hola {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Adios {username}') 
        elif user_message.lower() == "tell me a joke": 
            joke = random.choice(list(jokes_responses.keys()))
            response = jokes_responses[joke]
            await message.channel.send(f'{joke}\n\n{response}')

# Argument to run the bot by calling an event #         
client.run(token)  
