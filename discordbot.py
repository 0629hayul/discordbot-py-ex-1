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
	embedVar = discord.Embed(title="telum-명령어", description="* 접두사:`(따옴표X)")
	embedVar.add_field(value="call : 봇 실행 여부 확인", inline=False)
	embedVar.add_field(value="`help : 기본 명령어 확인", inline=False)
	embedVar.add_field(value="`hi : 인사", inline=False)
	embedVar.add_field(value="`hello : 멘션 기능 구현중", inline=False)

        await message.channel.send(embed=embedVar)
        
    if (command === 'avatar') {
		if (args[0]) {
			const user = getUserFromMention(args[0]);
			if (!user) {
				return message.reply('Please use a proper mention if you want to see someone elses avatar.');
			}

			return message.channel.send(`${user.username}'s avatar: ${user.displayAvatarURL({ dynamic: true })}`);
		}

		return message.channel.send(`${message.author.username}, your avatar: ${message.author.displayAvatarURL({ dynamic: true })}`);
	}
});
            
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
