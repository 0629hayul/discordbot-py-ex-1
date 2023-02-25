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
      
    if message.content == f'{PREFIX}멤버등록':
        await message.channel.send('멤버등록은 <#1077925680903376896>을 참고해주세요!')
    
    if message.content == f'{PREFIX}등업':
        embedVar = discord.Embed(title="등업 규칙", color=0x0094ff)
        embedVar.add_field(name="",value="- 서버개설 : teluny",inline=False)
        embedVar.add_field(name="",value="- 누적 50명 초대시 : telum",inline=False)
        embedVar.add_field(name="",value="- 누적 30명 초대시 : admin",  inline=False)
        embedVar.add_field(name="",value="- 5회 구매 : VIP", inline=False)
        embedVar.add_field(name="",value="- 1회 구매 : buyer", inline=False)
        embedVar.add_field(name="",value="- 서버참여 : member", inline=False)

        await message.channel.send(embed=embedVar)
    
    
    if message.content == f'{PREFIX}acc':
        embedVar = discord.Embed(title="계정 구매", color=0x0094ff)
        embedVar.add_field(name="구매 가능한 계정",value="- <#1078830041984684194>", inline=False)
        embedVar.add_field(name="",value="- <#1078830400304066640>", inline=False)
        embedVar.add_field(name="구매",value="<#1078652866165743676>를 참고해주세요", inline=False)
        embedVar.add_field(name="",value="기타 질문은 [teluny]유저 DM or <#1078829814619840642>에 문의주세요. 감사합니다 :)", inline=False)

        await message.channel.send(embed=embedVar)     
        
    if message.content == f'{PREFIX}순위':
        embedVar = discord.Embed(title="역할 순위", color=0x0094ff)
        embedVar.add_field(name="",value="[ teluny ]", inline=False)
        embedVar.add_field(name="",value="[ telum ]", inline=False)
        embedVar.add_field(name="",value="[ admin ]",inline=False)
        embedVar.add_field(name="",value="[ VIP ]", inline=False)
        embedVar.add_field(name="",value="[ buyer ]",  inline=False)
        embedVar.add_field(name="",value="[ member ]",inline=False)

        await message.channel.send(embed=embedVar)     
      

    if message.content.startswith(f'{PREFIX}ㅎㅇ'):
        await message.channel.send('hi, {0.author.mention}!'.format(message))

    if message.content == f'{PREFIX}help':
        embedVar = discord.Embed(title="Telum_bot", color=0x0094ff)
        embedVar.add_field(name="*접두사 :ㅤ.",value="- help : telum 봇 명령어 확인", inline=False)
        embedVar.add_field(name="",value="- 멤버등록 : 서버에 처음 들어오셨다면 멤버등록을 해주세요!", inline=False)
        embedVar.add_field(name="",value="- 등업 : 등업 규칙", inline=False)
        embedVar.add_field(name="",value="- 순위 : 역할 순위", inline=False)
        embedVar.add_field(name="",value="- acc : 계정 구매 도움말", inline=False)
        embedVar.add_field(name="",value="- evt : 이벤트 일정", inline=False)

        await message.channel.send(embed=embedVar)
  

    if message.content == f'{PREFIX}evt':
        embedVar = discord.Embed(title="이벤트 일정", color=0x0094ff)
        embedVar.add_field(name="",value="- 발로란트 무료 계정 이벤트(준비중) - <#1078846897445408839>", inline=False)

        await message.channel.send(embed=embedVar)
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
