from cmath import log
from distutils.sysconfig import PREFIX
import discord
import random
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']
VGEN = ['1leuila : seacow09',
'squareredbo : Ramabada95!',
'812138689 : Syxjcw10',
'ELGC07 : Jesesito07',
'Livais126 : 9511640004levi',
'oussama94400 : O$21296Os',
'acox7194 : scar2012',
'asesino5442 : tuputamadre1234',
'insidexis : stayinsideme5',
'ivanezemeza : Neftali1237',
'jigoku669 : tequiero96',
'jarinsmith07 : 1234qwer',
'Joan12a : pines16t1',
'eltakis193 : JOSEluis04',
'75529955 : a123a123',
'motley16 : rockeros123',
'jhonnytisca : Jhonny121096',
'oapm : oscarin78',
'jkauns : Venado123',
'Manatik0 : Manuel69',
'812138689 : Syxjcw10',
'issei71995 : alberto7',
'jlvcc : Jlvlink1@',
'harryhaharry : darkness123',
'jaehun0120 : wogns1130',
'jamg1819 : 100%alexis',
'jlvcc : Jlvlink1@',
'jeser546 : togurt12',
'ELIZZATH : N3vL_3PPTGSR,tE',
'mushrooms23635 : 45aelihm53',
'Manatik0 : Manuel69',
'DONIXXXD : gokuolA123',
'daniangrypants : Lastres21041998',
'ivandsc05 : ysxcun88',
'lechogat2251 : guajolocombo24',
'joelsuarezb1 : 24630571aa',
'lagzilla1 : Wolfenstine1',
'antisus100 : anachy100',
'Kaname1996k : Alaplaya13',
'dzidexi99 : 512939311W',
'jeroen38 : only1isme',
'DONIXXXD : gokuolA123',
'motley16 : rockeros123',
'lgzuspro : elculodelesli2',
'DONIXXXD : gokuolA123',
'artchronicles : Property_99',
'acox7194 : scar2012',
'yitaniden : dmc513ps3',
'vhalair : megamanX3',
'swliemp : Happy123',
'hellablayzed : Saitek45',
'zskesha7 : taylorgangordie1',
'rocke34321 : elboy12345',
'jonohl2 : s9o8mfh94',
'akumatdk2 : bethwen3003',
'JDanRS : LinkMaster99',
'acno974 : deviljin01',
'JovanyLOPEZ : jjlq007sge9',
'rocke34321 : elboy12345',
'nowik9 : paker123',
'Livais126 : 9511640004levi',
'aurora11x : deepfear35',
'josemau666 : Boris1996',
'pikaniplay : 123weasdxc',
'DONIXXXD : gokuolA123',
'gorian770 : Gorian98',
'icmarg : Marl0n20',
'fashionvlam : 110088wai',
'kev5641 : Emachines123',
'i7guerra : iwarbiker1',
'JDanRS : LinkMaster99',
'jigoku669 : tequiero96',
'jortuone182 : MEMELOL182',
'pikaj3wz : Sadmonkey202',
'swliemp : Happy123',
'motley16 : rockeros123',
'theblazedbehr : Behr813425',
'aurora11x : deepfear35',
'asesino5442 : tuputamadre1234',
'mvc3502 : 1621carrelhas',
'alpi58 : alperbey123',
'jhonnytisca : Jhonny121096',
'lyxup6 : money131',
'jullcom : Dinosaurios05',
'icmarg : Marl0n20',
'vhalair : megamanX3',
'issei71995 : alberto7',
'lgzuspro : elculodelesli2',
'bigturtle3 : malvados1',
'hellkan89 : Mipapa150689',
'lgzuspro : elculodelesli2',
'jamg1819 : 100%alexis',
'bjbinge : ATVatv123',
'JDanRS : LinkMaster99',
'jullcom : Dinosaurios05',
'ricardohammerl : salat123',
'jlvcc : Jlvlink1@',
'jortuone182 : MEMELOL182',
'antisus100 : anachy100',
'ELGC07 : Jesesito07',
'Kaname1996k : Alaplaya13',
'jarinsmith07 : 1234qwer',
'irvingpe : sableyemega13',
'jigoku669 : tequiero96',
'jigoku669 : tequiero96',
'JASTRALNIGHTMARE : equipoNoble6',
'gennaitianyi : breakfast876',
'ELGC07 : Jesesito07',
'mdcs0024 : firestrike89',
'khaysjr2 : central30',
'mushrooms23635 : 45aelihm53',
'JonathanNorberto : CLUBPENGUIN07',
'texascow12 : Passw0rd2003',
'bigturtle3 : malvados1',
'jeser546 : togurt12',
'gennaitianyi : breakfast876',
'ivandsc05 : ysxcun88',
'icmarg : Marl0n20',
'icek54 : esgugas54',
'kenken517 : kenken517',
'pikaniplay : 123weasdxc',
'gorian770 : Gorian98',
'P3ZSTEVE : oscaring1',
'leuila : seacow09',
'i7guerra : iwarbiker1',
'idoserwave : 15101982Nix',
'joselc36 : rose36',
'idoserwave : 15101982Nix',
'Yisus1220 : Corrales32',
'goliath140397 : 640181-g',
'jeroen38 : only1isme',
'ivandsc05 : ysxcun88',
'Imranotelli : imran2004',
'jorgeadt2 : sabinas1995',
'irvingpe : sableyemega13',
'nekid33 : benoit62110',
'mdcs0024 : firestrike89',
'yitaniden : dmc513ps3',
'jamg1819 : 100%alexis',
'bigturtle3 : malvados1',
'roostt0 : theringx2',
'jigoku669 : tequiero96',
'jpg1450 : agosto1450',
'yesid133 : ximena123',
'jpg1450 : agosto1450',
'nanadyia : 12021997Manon',
'idoserwave : 15101982Nix',
'irwin061220 : a1e2i3o4u5',
'zerlerger1 : Sebastiangallas123',
'DsTPiXeLeD : 1020424a',
'rocke34321 : elboy12345',
'zskesha7 : taylorgangordie1',
'jamg1819 : 100%alexis',
'stedek : Omsk1993',
'ELGC07 : Jesesito07',
'MisatoSoryu : Narutoyhinata02',
'jacek19952 : koper101',
'seanpepper@shaw.ca : jetset82',
'Imranotelli : imran2004',
'jmcazero : jhan1992',
'acox7194 : scar2012',
'heavymetalus : masterspy230186',
'anthonysareis1011 : Santhony557',
'motley16 : rockeros123',
'ELIZZATH : N3vL_3PPTGSR,tE',
'ismael338558 : 20052005Is1234',
'jlvcc : Jlvlink1@',
'hellablayzed : Saitek45',
'Yisus1220 : Corrales32',
'812138689 : Syxjcw10',
'lgzuspro : elculodelesli2',
'ivandsc05 : ysxcun88',
'kinosage : wynchu6776',
'812138689 : Syxjcw10',
'venefeci123 : Darkknight23',
'i7guerra : iwarbiker1',
'bigturtle3 : malvados1',
'rakoon_28@hotmail.com : meastro',
'lamga123 : lamga123',
'hellkan89 : Mipapa150689',
'issei71995 : alberto7',
'MisatoSoryu : Narutoyhinata02',
'ivandsc05 : ysxcun88',
'jesusnovelo917 : jesusnovelo9',
'ELGC07 : Jesesito07',
'matrasblya : qqwweerr11',
'asesino5442 : tuputamadre1234',
'ELGC07 : Jesesito07',
'venefeci123 : Darkknight23',
'ivandsc05 : ysxcun88',
'jigoku669 : tequiero96',
'pikaniplay : 123weasdxc',
'mrkpot999 : 2450167a',
'doitmaik : jelizandro290',
'rizity28 : obeys382',
'utayski : Majutay17',
'devedeu63 : Daviduca123',
'ELGC07 : Jesesito07',
'i7guerra : iwarbiker1',
'akumatdk2 : bethwen3003',
'habot30 : javii974',
'Locogaymer12 : pepillo12',
'Yisus1220 : Corrales32',
'habot30 : javii974',
'Imranotelli : imran2004',
'cph3i : Lastres21041998',
'rocke34321 : elboy12345',
'idoserwave : 15101982Nix',
'kinosage : wynchu6776',
'ssgamer000 : sousou2006',
'stedek : Omsk1993',
'yitaniden : dmc513ps3',
'ivandsc05 : ysxcun88',
'idoserwave : 15101982Nix',
'jullcom : Dinosaurios05',
'icek54 : esgugas54',
'DJTr3k50 : 1ZaqwsxcderfV2',
'insidexis : stayinsideme5',
'kyraalia : Kenny185',
'maramoscabral : 430416Aq@',
'jhardi99 : ginel2002',
'zerlerger1 : Sebastiangallas123',
'zerlerger1 : Sebastiangallas123',
'insidexis : stayinsideme5',
'jpg1450 : agosto1450',
'bjbinge : ATVatv123',
'roostt0 : theringx2',
'jesusflores456 : Sleepingdogs4',
'pikaniplay : 123weasdxc',
'jullcom : Dinosaurios05',
'eltakis193 : JOSEluis04',
'schnellunnerwegs : tn1910002474',
'bjbinge : ATVatv123',
'draxxes1992 : Daniel1992',
'Daniel1992 : breakfast876',
'icmarg : Marl0n20',
'kev5641 : Emachines123',
'seanpepper@shaw.ca : jetset82',
'i7guerra : iwarbiker1',
'pikaniplay : 123weasdxc',
'jeroen38 : only1isme',
'MisatoSoryu : Narutoyhinata02',
'draxxes1992 : Daniel1992',
'bukananggora : TOMbrother17',
'ELIZZATH : N3vL_3PPTGSR,tE',
'dongshlonger69 : Beemer345',
'jancerem : Jancarlos1000',
'P3ZSTEVE : oscaring1',
'john54555 : Id9493279',
'rocke34321 : elboy12345',
'issei71995 : alberto7',
'jullcom : Dinosaurios05',
'75529955 : a123a123',
'isaaconofre : Isaac990323',
'P3ZSTEVE : oscaring1',
'jhardi99 : ginel2002',
'cph3i : Lastres21041998',
'JovanyLOPEZ : jjlq007sge9',
'Jaskper : notbook123',
'swliemp : Happy123',
'jacek19952 : koper101',
'swliemp : Happy123',
'insidexis : stayinsideme5',
'jaimaqueo : 55458825Jai',
'jarinsmith07 : 1234qwer',
'jesusflores456 : Sleepingdogs4',
'jarinsmith07 : 1234qwer',
'lechogat2251 : guajolocombo24',
'ethanhitchner : fallacorn1',
'jancerem : Jancarlos1000',
'alessio99bro : Arcobalen0',
'i7guerra : iwarbiker1',
'ELGC07 : Jesesito07',
'asesino5442 : tuputamadre1234',
'superdanut : Visandanut123',
'oussama94400 : O$21296Os',
'BlackMadnesS98 : Gatewayts98',
'i7guerra : iwarbiker1',
'ELIZZATH : N3vL_3PPTGSR,tE',
'devedeu63 : Daviduca123',
'insidexis : stayinsideme5',
'juanma51 : 220190kfp',
'jlvcc : Jlvlink1@',
'Yisus1220 : Corrales32',
'mostlyawsm7 : cataztrophe1993',
'Calambria : fernando9090',
'Calambria : fernando9090',
'lgzuspro : elculodelesli2',
'yitaniden : dmc513ps3',
'i7guerra : iwarbiker1',
'JDanRS : LinkMaster99',
'Manatik0 : Manuel69',
'elkoofficial : 95409540KQxY',
'asesino5442 : tuputamadre1234',
'irvingpe : sableyemega13',
'Livais126 : 9511640004levi',
'issei71995 : alberto7',
'insidexis : stayinsideme5',
'jeroen38 : only1isme',
'rocke34321 : elboy12345',
'lamga123 : lamga123',
'swliemp : Happy123',
'ymz3006 : ymz20000311',
'nicceli98 : pohjola120',
'john54555 : Id9493279',
'pikaniplay : 123weasdxc',
'xbisom : 1370537junior',
'jigoku669 : tequiero96',
'juanma51 : 220190kfp',
'nekid33 : benoit62110',
'jdrama418 : 504bfrank05',
'JonathanNorberto : CLUBPENGUIN07',
'DONIXXXD : gokuolA123',
'ivanezemeza : Neftali1237',
'jpg1450 : agosto1450',
'idoserwave : 15101982Nix',
'laya9910 : sinaloa0',
'ELGC07 : Jesesito07',
'isaaconofre : Isaac990323',
'stedek : Omsk1993',
'rocke34321 : elboy12345',
'jekave901 : nikolas1',
'cph3i : Lastres21041998',
'MisatoSoryu : Narutoyhinata02',
'jamg1819 : 100%alexis',
'jesusnovelo917 : jesusnovelo9',
'JASTRALNIGHTMARE : equipoNoble6',
'hellkan89 : Mipapa150689',
'DONIXXXD : gokuolA123',
'ivanguti113 : 1q2w3e4r',
'jeser546 : togurt12',
'issei71995 : alberto7',
'swliemp : Happy123',
'eltakis193 : JOSEluis04',
'akumatdk2 : bethwen3003',
'irvingpe : sableyemega13',
'ivanguti113 : 1q2w3e4r',
'rocke34321 : elboy12345',
'Jaskper : notbook123',
'hellablayzed : Saitek45',
'seanpepper@shaw.ca : jetset82',
'Calambria : fernando9090',
'bigturtle3 : malvados1',
'i7guerra : iwarbiker1',
'irvingpe : sableyemega13',
'isaaconofre : Isaac990323',
'irvingpe : sableyemega13',
'DONIXXXD : gokuolA123',
'jorgeadt2 : sabinas1995',
'jullcom : Dinosaurios05',
'stedek : Omsk1993',
'insidexis : stayinsideme5',
'jpg1450 : agosto1450',
'Imranotelli : imran2004',
'ethanhitchner : fallacorn1',
'josemau666 : Boris1996',
'icmarg : Marl0n20',
'raul_marios@yahoo.com : 369369',
'jpg1450 : agosto1450',
'i7guerra : iwarbiker1',
'ELGC07 : Jesesito07',
'Imranotelli : imran2004',
'insidexis : stayinsideme5',
'DzEduJr : esemeok12',
'Jaskper : notbook123',
'jdrama418 : 504bfrank05',
'jullcom : Dinosaurios05',
'jacek19952 : koper101',
'hellkan89 : Mipapa150689',
'swliemp : Happy123',
'icmarg : Marl0n20',
'Livais126 : 9511640004levi',
'P3ZSTEVE : oscaring1',
'kenken517 : kenken517',
'vhalair : megamanX3',
'gorian770 : Gorian98',
'lagzilla1 : Wolfenstine1',
'roostt0 : theringx2',
'jesusnovelo917 : jesusnovelo9',
'pikaniplay : 123weasdxc',
'issei71995 : alberto7',
'jacek19952 : koper101',
'jkauns : Venado123',
'swliemp : Happy123',
'DzEduJr : esemeok12',
'acox7194 : scar2012',
'issei71995 : alberto7',
'theboomer8888 : 12q12q12q',
'Manatik0 : Manuel69',
'stedek : Omsk1993',
'zerlerger1 : Sebastiangallas123',
'vhalair : megamanX3',
'seanpepper@shaw.ca : jetset82',
'Manatik0 : Manuel69',
'xmyuu3 : nevim123456',
'skiluvuador : lucasfoda88',
'jesusflores456 : Sleepingdogs4',
'jeser546 : togurt12',
'icmarg : Marl0n20',
'swliemp : Happy123',
'jullcom : Dinosaurios05',
'hayashii21:wlakopassword21']
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
            
    if message.content == f'{PREFIX}gen':
        await message.channel.send(random.choice(VGEN))         

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
