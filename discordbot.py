from cmath import log
from distutils.sysconfig import PREFIX
import discord
import random
import base64
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
import os
import requests
import time
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
    if message.content.startswith('!입금'):
        # 입금주명 입력받기
        await message.channel.send('입금주명을 입력하세요.')
        def check_author(m):
            return m.author == message.author and m.channel == message.channel
        try:
            name = await client.wait_for('message', timeout=120.0, check=check_author)
            name = name.content
        except asyncio.TimeoutError:
            await message.channel.send('입금주명 입력 시간이 초과되었습니다.')
            return
        
        # 입금액 입력받기
        await message.channel.send('입금할 금액을 입력하세요.')
        try:
            amount = await client.wait_for('message', timeout=120.0, check=check_author)
            amount = int(amount.content)
        except asyncio.TimeoutError:
            await message.channel.send('입금액 입력 시간이 초과되었습니다.')
            return
        
        # 토스 API를 이용하여 입금 확인
        # API 토큰과 토스 계좌번호는 개발자센터에서 발급 받아 사용합니다.
        url = 'https://toss.im/transfer-web/linkgen-api/link'
        headers = {'Authorization': 'test_sk_MGjLJoQ1aVZYe46dDlg3w6KYe2RN'}
        data = {
            'amount': amount,
            'bankName': '토스뱅크',
            'bankAccountNo': '토스뱅크 1908-8896-4321',
            'message': 'discord.py 입금 확인'
        }
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        
        # 입금 확인 결과 출력
        if result['resultCode'] == 'SUCCESS':
            await message.channel.send('확인 되었습니다.')
        else:
            await message.channel.send('입금 확인에 실패했습니다.')
##########################################################################################################################################            
    if message.content == f'{PREFIX}멤버등록':
        await message.channel.send('멤버등록은 <#1077925680903376896>을 참고해주세요!')
   
    if message.content == f'{PREFIX}tb':
        a = 1;
        await message.channel.send('<@819436785998102548> 잠시만 기다려주세요. 대기열 확인 후 게임시작합니다.')
  

    if message.content == f'{PREFIX}게임':
        if message.author.id == 819436785998102548:
            await message.channel.send('게임 시작!')
            sleep(1)
            await message.channel.send('플레이어님은 1,2중에 하나를 선택해주세요.')
        else:
            await message.channel.send('관리자(<@819436785998102548>)가 게임을 시작해야합니다. 관리자를 호출해주세요.')
    if message.content == f'{PREFIX}1':
        if message.author.id == 819436785998102548:
            await message.channel.send('teluny : 1')
            sleep(1)
            await message.channel.send('plyer : 2')
            sleep(1)
            await message.channel.send('숫자를 정하셨으면 “시작”을 해주세요.')
        else:
            await message.channel.send('teluny : 2')
            sleep(1)
            await message.channel.send('plyer : 1')
            sleep(1)
            await message.channel.send('숫자를 정하셨으면 “시작”을 해주세요.')

    
    if message.content == f'{PREFIX}2':
        if message.author.id == 819436785998102548:
            await message.channel.send('teluny : 2')
            sleep(1)
            await message.channel.send('plyer : 1')
            sleep(1)
            await message.channel.send('숫자를 정하셨으면 “시작”을 해주세요.')
        else:
            await message.channel.send('teluny : 1')
            sleep(1)
            await message.channel.send('plyer : 2')
            sleep(1)
            await message.channel.send('숫자를 정하셨으면 “시작”을 해주세요.')
            

    if message.content == f'{PREFIX}시작':
        if message.author.id == 819436785998102548:
            await message.channel.send('랜덤숫자를 뽑는중입니다.')
        else:
            await message.channel.send('관리자(<@819436785998102548>)가 시작해야합니다.')         
     
        
    if message.content == f'{PREFIX}?':
        await message.channel.send('<#1078986719556284446>을 참고해주세요.\n질문은 <@819436785998102548> DM 혹은 <#1080448082526871564>에서 부탁드립니다 :)')
        
   
    if message.content == f'{PREFIX}등업':
        embedVar = discord.Embed(title="등업 규칙", color=0x0094ff)
        embedVar.add_field(name="",value="- 서버개설 : teluny",inline=False)
        embedVar.add_field(name="",value="- 누적 50명 초대시 : telum",inline=False)
        embedVar.add_field(name="",value="- 누적 30명 초대시 : admin",  inline=False)        
        embedVar.add_field(name="",value="- 10회 구매 : VVIP", inline=False)
        embedVar.add_field(name="",value="- 5회 구매 : VIP", inline=False)
        embedVar.add_field(name="",value="- 1회 구매 : buyer", inline=False)
        embedVar.add_field(name="",value="- 서버참여 : member", inline=False)

        await message.channel.send(embed=embedVar)
    
    
    if message.content == f'{PREFIX}acc':
        embedVar = discord.Embed(title="계정 구매", color=0x0094ff)
        embedVar.add_field(name="구매 가능한 계정",value="- <#1078830041984684194>", inline=False)
        embedVar.add_field(name="",value="- <#1078830400304066640>", inline=False)
        embedVar.add_field(name="구매",value="<#1078960264059293696>를 참고해주세요", inline=False)
        embedVar.add_field(name="냥코&발로 계정 이벤트",value="evt를 참고해주세요", inline=False)
        embedVar.add_field(name="",value="기타 질문은 <@819436785998102548> DM or <#1080448082526871564>에 문의주세요. 감사합니다 :)", inline=False)

        await message.channel.send(embed=embedVar)  
        
    if message.content == f'{PREFIX}tkt':
        embedVar = discord.Embed(title="서버 티켓", color=0x0094ff)
        embedVar.add_field(name="티켓 사용",value="- 티켓 사용 용도는 계정 구매/teluny쿠폰구매/teluny쿠폰환전/기타질문 용도로만 사용해주세요.", inline=False)
        embedVar.add_field(name="주의점",value="티켓을 실수로 닫으면 재오픈/삭제가 가능합니다. \n재오픈 요청시 <#1078836298229502063>에서 <@819436785998102548>에게 재오픈 요청 혹은 DM으로 재오픈 요청을 해주세요.", inline=False)
        embedVar.add_field(name="",value="기타 질문은 <@819436785998102548> DM or <#1080448082526871564>에 문의주세요. 감사합니다 :)", inline=False)

        await message.channel.send(embed=embedVar)  
        
    if message.content == f'{PREFIX}순위':
        embedVar = discord.Embed(title="역할 순위", color=0x0094ff)
        embedVar.add_field(name="",value="[ teluny ]ㅤ👑", inline=False)
        embedVar.add_field(name="",value="[ telum ]ㅤ♾️", inline=False)
        embedVar.add_field(name="",value="[ admin ]ㅤ🌐",inline=False)
        embedVar.add_field(name="",value="[ VVIP ]ㅤ💎", inline=False)
        embedVar.add_field(name="",value="[ VIP ]ㅤ💝", inline=False)
        embedVar.add_field(name="",value="[ buyer ]ㅤ💸",  inline=False)
        embedVar.add_field(name="",value="[ member ]ㅤ🤍",inline=False)

        await message.channel.send(embed=embedVar)     
      


    if message.content == f'{PREFIX}help':
        embedVar = discord.Embed(title="Telum_bot", color=0x0094ff)
        embedVar.add_field(name="*접두사 :ㅤ.",value="- help : telum 봇 명령어 확인", inline=False)
        embedVar.add_field(name="",value="- 멤버등록 : 서버에 처음 들어오셨다면 멤버등록을 해주세요!", inline=False)
        embedVar.add_field(name="",value="- 등업 : 등업 규칙", inline=False)
        embedVar.add_field(name="",value="- 순위 : 역할 순위", inline=False)
        embedVar.add_field(name="",value="- acc : 계정 구매 도움말", inline=False)
        embedVar.add_field(name="",value="- evt : 이벤트 일정", inline=False)
        embedVar.add_field(name="",value="- tkt : 티켓 사용 도움말", inline=False)

        await message.channel.send(embed=embedVar)
  

    if message.content == f'{PREFIX}evt':
        embedVar = discord.Embed(title="이벤트 일정", color=0x0094ff)
        embedVar.add_field(name="",value="- 발로란트 계정 2+1 이벤트 - <#1078846897445408839>", inline=False)
        embedVar.add_field(name="",value="- 냥코 계좌&문상 50% 할인 이벤트! - <#1078962629353148486>", inline=False)
        embedVar.add_field(name="",value="- 초대 이벤트(최대 문상18,000원+냥&발로계정!) - <#1078982517098561556>", inline=False)
        embedVar.add_field(name="",value="- 멤버이벤트 이벤트! 존버만타도 문상 최대 185,000원! - <#1079027442439692438>", inline=False)

        await message.channel.send(embed=embedVar)
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
