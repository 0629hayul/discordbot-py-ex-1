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

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")
        
            if message.content == f'{PREFIX}embed':
        embed=discord.Embed(title="embed messege test", description="hello world")
        embed.add_field(name="undefined", value="undefined", inline=False)
        await ctx.send(embed=embed)

    if message.content.startswith(f'{PREFIX}hello'):
    @commands.command(pass_context=True)
    async def hug(self, ctx):
        await self.bot.say("hello, {}!".format(ctx.message.author.mention))

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
