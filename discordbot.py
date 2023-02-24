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
    if message.content.startswith(f'{PREFIX}hi'):
        await message.channel.send("hi!")
        
    if message.content == f'call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.send('{0.author.mention} Hello!'.format(message))

    if message.content == f'{PREFIX}help':
        embedVar = discord.Embed(title="Telum_bot", color=0x3B3B3B)
        embedVar.add_field(name="*접두사 : .",value="- .help : telum 봇 명령어 확인", inline=False)
        embedVar.add_field(name="",value="- .hi : 인사", inline=False)
        embedVar.add_field(name="",value="- .hello : 멘션 기능 구현중", inline=False)
        embedVar.add_field(name="",value="- call : (접두사X)봇 확인", inline=False)
        await message.channel.send(embed=embedVar)
        
            
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
