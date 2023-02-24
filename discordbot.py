from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == f'call':
        await message.channel.send("callback!")
    
    if message.content == f'test':
        await message.channel.send('<#1077856697525219381>')

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('hello, {0.author.mention}!'.format(message))

    if message.content == f'{PREFIX}help':
        embedVar = discord.Embed(title="Telum_bot", color=0x3B3B3B)
        embedVar.add_field(name="*접두사 :ㅤ.",value="- help : telum 봇 명령어 확인", inline=False)
        embedVar.add_field(name="",value="- hello : 인사", inline=False)
        embedVar.add_field(name="",value="- call : (접두사X)봇 확인", inline=False)
        await message.channel.send(embed=embedVar)
        
        newUserMessage = """
You
can
put
your
multiline
message
here!
"""

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try: 
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title="Welcome "+member.name+"!"
        color=discord.Color.green()
    )
        
    role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await client.add_roles(member, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title="😢 Goodbye "+member.name+"!",
        description="Until we meet again old friend." # A description isn't necessary, you can delete this line if you don't want a description.
        color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    )
            
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
