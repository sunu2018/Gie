# -*- coding: utf-8 -*-

from gyevha import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
 
# Ini Untuk Login Via Lik Dan Via Emal
#gye = LINE()
#gye = LINE("Email","Password")
#gye.log("Auth Token : " + str(gye.authToken))
#channelToken = gye.getChannelResult()
#gye.log("Channel Token : " + str(channelToken))

# Silahkan Edit Sesukamu
# Asalkan Rapih Dan Respon
# jika ingin login Via qr Ganti Saja
# Atau Login Via Emal
# Mudeng Orang kalo Ra Mudeng
# Sungguh Terlalu
# Jangan Lupa Add Admin 
# id Line ( aisyagye )
#==============================================================================#
botStart = time.time()
#kalo mau login code qr disini pake
#gye = LINE()
#gye.log("Auth Token : " + str(gye.authToken))
#channelToken = gye.getChannelResult()
#gye.log("Channel Token : " + str(channelToken))

#ais = LINE()
#ais.log("Auth Token : " + str(ais.authToken))
#channelToken = ais.getChannelResult()
#ais.log("Channel Token : " + str(channelToken))

#ki2 = LINE()
#ki2.log("Auth Token : " + str(ki2.authToken))
#channelToken = ki2.getChannelResult()
#ki2.log("Channel Token : " + str(channelToken))

#ki3 = LINE()
#ki3.log("Auth Token : " + str(ki3.authToken))
#channelToken = ki3.getChannelResult()
#ki3.log("Channel Token : " + str(channelToken))

#ki4 = LINE()
#ki4.log("Auth Token : " + str(ki4.authToken))
#channelToken = ki4.getChannelResult()
#ki4.log("Channel Token : " + str(channelToken))

#kalo mau login menggunakan token
#gunakan disini hapus tanda pagarnya 
#yg atas dinpagar atau bisa juga token di atas 
#di dalam tanda LINE ("TOKEN MU ")

gye = LINE("Et5gYrvSnIEOpWFK5m4f.4YSrMg2oNLZ3c2qS97Qi+W.fsNClszZfRIpi5y3C/DKfbTqc100zzXX0tWv5M3TZ/k=")
ais = LINE("EtQQZ5O8Q9ZNn47rzMCd.ZumT2/Y29n7tOJ4IwPo4tq.1TFAsQAvYzlyAp1XEM5RsdIZwZtoEnir3y6dea1fo1E=")
ki2 = LINE("Et0Oj6SRTe8eGtw9jK3d.SPS+quoffhJbcv30K1vAdq.gD9LSFBUBorGs552hX0ltdIVxai6oaF/Ox4aGWcOFJA=")
ki3 = LINE("EtZREl8uhl6VAapUjlTc.WSbM8Imh8gKzhGhc98UuVa.feeQQaWBEpieqDeI+TBL9t7uKaW9tBVFmRZfAB9tHUk=")
ki4 = LINE("EtRhFIGABsjUHKYKVoqe.lVN3XpWByvHZ/lHSAQFaBG.Fo8l69iIhSLOiMhTWoKoj6JIgftT7HEjwC0RykLYwZc=")


KAC = [gye,ais,ki2,ki3,ki4]
GUE = [ais,ki2,ki3,ki4]  #ini jangan luh hapus peak ini fungsi Ciak alias kick
#maksudnya agar bot sb/induk gak ikutan nge kick Mudeng ora
gyeMID = gye.profile.mid
aisMID = ais.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
Bots = [gyeMID,aisMID,ki2MID,ki3MID,ki4MID]# ini jangan dinrubah Gunanya agar bot tidak saling kick
creator = ["u104e95aaefb53cf411f77353f6a96ece"]
Owner = ["u104e95aaefb53cf411f77353f6a96ece"]
admin = ["u104e95aaefb53cf411f77353f6a96ece"]

gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()
ki2Profile = ki2.getProfile()
ki2Profile = ki3.getProfile()
ki2Profile = ki4.getProfile()

lineSettings = gye.getSettings()
aisSettings = ais.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()

oepoll = OEPoll(gye)
oepoll1 = OEPoll(ais)
oepoll2 = OEPoll(ki2)
oepoll3 = OEPoll(ki3)
oepoll4 = OEPoll(ki4)

responsename = gye.getProfile().displayName
responsename2 = ais.getProfile().displayName
responsename3 = ki2.getProfile().displayName
responsename2 = ki3.getProfile().displayName
responsename3 = ki4.getProfile().displayName
#==============================================================================#
#==============================================================================#
settings = {
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"บัญชีนี้ได้การป้องกันโดย PZGuard ระบบได้ทำการบล็อคคุณอัตโนมัติ",
    "comment":"Thanks for add me",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

user1 = gyeMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = gye.getProfile() 
backup = gye.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง","@พี่อาร์ท","@ATR","ขอคลิปหน่อยครับ"]

myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def Rapid1Say(mtosay):
    gye.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       gye.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    gye.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, gyeMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(gyeMID)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp = "╭════✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰   " + "\n" \
                  "║About" + "\n" + \
                  "║Help media" + "\n" + \
                  "║Help kicker" + "\n" + \
                  "║Help group" + "\n" + \
                  "║Help protect" + "\n" + \
                  "║Help setting" + "\n" + \
                  "║textTospeech" + "\n" + \
                  "║Languange" + "\n" + \
                  "║Me" + "\n" + \
                  "║Mymid" + "\n" + \
                  "║Myname" + "\n" + \
                  "║Mybio" + "\n" + \
                  "║Mypict" + "\n" + \
                  "║Mycover" + "\n" + \
                  "║Myvideo" + "\n" + \
                  "║Mid" + "\n" + \
                  "║Name" + "\n" + \
                  "║Bio" + "\n" + \
                  "║Pict" + "\n" + \
                  "║Cover" + "\n" + \
                  "║Video" + "\n" + \
                  "║Copy" + "\n" + \
                  "║Restore" + "\n" + \
                  "║Mimic on/off" + "\n" + \
                  "║MimicList" + "\n" + \
                  "║MimicAdd" + "\n" + \
                  "║MimicDel" + "\n" + \
                  "║Broadcastvoice" + "\n" + \
                  "║Cbroadcastvoice" + "\n" + \
                  "║Restart" + "\n" + \
                  "║Runtime" + "\n" + \
                  "╰════"
    return myHelp
def listgrup():
    listGrup = "╭════HelpGroup " + "\n" + \
                  "║GroupCreator" + "\n" + \
                  "║GroupId" + "\n" + \
                  "║GroupName" + "\n" + \
                  "║GroupPicture" + "\n" + \
                  "║GroupList" + "\n" + \
                  "║GroupMemberList" + "\n" + \
                  "║GroupInfo" + "\n" + \
                  "║Url" + "\n" + \
                  "║Link on/off" + "\n" + \
                  "║Gurl" + "\n" + \
                  "║Friendlist" + "\n" + \
                  "║Blocklist" + "\n" + \
                  "║Friendlist mid" + "\n" + \
                  "║Invite:gcreator" + "\n" + \
                  "║Spam on/off" + "\n" + \
                  "║Reject inv" + "\n" + \
                  "║Allban" + "\n" + \
                  "║Grouplist" + "\n" + \
                  "║Blist" + "\n" + \
                  "║Mention" + "\n" + \
                  "║Lurking on" + "\n" + \
                  "║Lurking off" + "\n" + \
                  "║Lurking reset" + "\n" + \
                  "║Lurking" + "\n" + \
                  "║Invite" + "\n" + \
                  "║uninstall" + "\n" + \
                  "║Kick" + "\n" + \
                  "║Ban:on" + "\n" + \
                  "║Unban:on" + "\n" + \
                  "╰════"
    return listGrup
def socmedia():
    socMedia = "╭════HelpMedia " + "\n" + \
                  "║Instagram" + "\n" + \
                  "║Fotoig" + "\n" + \
                  "║Youtube" + "\n" + \
                  "║Music" + "\n" + \
                  "║Lyric" + "\n" + \
                  "║ScreenshootWebsite" + "\n" + \
                  "║Film:" + "\n" + \
                  "║Kalender" + "\n" + \
                  "║CheckDate" + "\n" + \
                  "║Textig" + "\n" + \
                  "║Wikipedia" + "\n" + \
                  "║Urban" + "\n" + \
                  "║Anime" + "\n" + \
                  "║Image" + "\n" + \
                  "║Pornhub" + "\n" + \
                  "╰════"
    return socMedia
      
def helpset():
    helpSet = "╭════HelpMySet " + "\n" + \
    "║ᴍʏ sᴇʟғ" + "\n" + \
    "║sᴏᴄᴍᴇᴅɪᴀ" + "\n" + \
    "║ʟɪsᴛ ɢʀᴜᴘ" + "\n" + \
    "║ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ" + "\n" + \
    "║ʟɪsᴛ ᴋɪᴄᴋᴇʀ" + "\n" + \
    "║sᴛᴀᴛᴜs" + "\n" + \
    "║ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
    "║ʟɪsᴛ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
    "╰════"
    return helpSet 

def helpkicker():
    helpKicker = "╭════HelpKicker " + "\n" + \
    "║K1 kick" + "\n" + \
    "║K2 kick" + "\n" + \
    "║K3 kick" + "\n" + \
    "║K1 invite" + "\n" + \
    "║K2 inv" + "\n" + \
    "║K3 vit" + "\n" + \
    "║K1 tag" + "\n" + \
    "║K1gruplist" + "\n" + \
    "║K2listgrup" + "\n" + \
    "║K3listrom" + "\n" + \
    "║Cleanse" + "\n" + \
    "║Scan blacklist" + "\n" + \
    "║cb" + "\n" + \
    "║Nameall:" + "\n" + \
    "║Bioall" + "\n" + \
    "╰════"
    return helpKicker
    
def helpsetting():
    helpSetting = "╭════SettingList " + "\n" + \
    "║Protect on/off" + "\n" + \
    "║Cancel pro on/off" + "\n" + \
    "║Invit pro on/off" + "\n" + \
    "║Link pro on/off" + "\n" + \
    "║Join pro on/off" + "\n" + \
    "║Proall on/off" + "\n" + \
    "║Autojoin on/off" + "\n" + \
    "║Autoadd on/off" + "\n" + \
    "║Autoleave on/off" + "\n" + \
    "║Autoread on/off" + "\n" + \
    "║Tag on/off" + "\n" + \
    "║Selfbot on/off" + "\n" + \
    "║Tag2 on/off" + "\n" + \
    "║Checksticker on/off" + "\n" + \
    "║Sider on/off" + "\n" + \
    "║Welcomemessage on/off" + "\n" + \
    "║Leavemessage on/off" + "\n" + \
    "╰════"
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   "╔══════════════┓" + "\n" + \
                         "╠⌬ ✰self protect✰    ⌬" + "\n" + \
                         "╚══════════════┛" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "          ʜᴇʟᴘ ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "╔══════════════┓" + "\n" + \
                         "╠❂ af : Afrikaans" + "\n" + \
                         "╠❂ sq : Albanian" + "\n" + \
                         "╠❂ ar : Arabic" + "\n" + \
                         "╠❂ hy : Armenian" + "\n" + \
                         "╠❂ bn : Bengali" + "\n" + \
                         "╠❂ ca : Catalan" + "\n" + \
                         "╠❂ zh : Chinese" + "\n" + \
                         "╠❂ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠❂ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠❂ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠❂ hr : Croatian" + "\n" + \
                         "╠❂ cs : Czech" + "\n" + \
                         "╠❂ da : Danish" + "\n" + \
                         "╠❂ nl : Dutch" + "\n" + \
                         "╠❂ en : English" + "\n" + \
                         "╠❂ en-au : English (Australia)" + "\n" + \
                         "╠❂ en-uk : English (United Kingdom)" + "\n" + \
                         "╠❂ en-us : English (United States)" + "\n" + \
                         "╠❂ eo : Esperanto" + "\n" + \
                         "╠❂ fi : Finnish" + "\n" + \
                         "╠❂ fr : French" + "\n" + \
                         "╠❂ de : German" + "\n" + \
                         "╠❂ el : Greek" + "\n" + \
                         "╠❂ hi : Hindi" + "\n" + \
                         "╠❂ hu : Hungarian" + "\n" + \
                         "╠❂ is : Icelandic" + "\n" + \
                         "╠❂ id : Indonesian" + "\n" + \
                         "╠❂ it : Italian" + "\n" + \
                         "╠❂ ja : Japanese" + "\n" + \
                         "╠❂ km : Khmer (Cambodian)" + "\n" + \
                         "╠❂ ko : Korean" + "\n" + \
                         "╠❂ la : Latin" + "\n" + \
                         "╠❂ lv : Latvian" + "\n" + \
                         "╠❂ mk : Macedonian" + "\n" + \
                         "╠❂ no : Norwegian" + "\n" + \
                         "╠❂ pl : Polish" + "\n" + \
                         "╠❂ pt : Portuguese" + "\n" + \
                         "╠❂ ro : Romanian" + "\n" + \
                         "╠❂ ru : Russian" + "\n" + \
                         "╠❂ sr : Serbian" + "\n" + \
                         "╠❂ si : Sinhala" + "\n" + \
                         "╠❂ sk : Slovak" + "\n" + \
                         "╠❂ es : Spanish" + "\n" + \
                         "╠❂ es-es : Spanish (Spain)" + "\n" + \
                         "╠❂ es-us : Spanish (United States)" + "\n" + \
                         "╠❂ sw : Swahili" + "\n" + \
                         "╠❂ sv : Swedish" + "\n" + \
                         "╠❂ ta : Tamil" + "\n" + \
                         "╠❂ th : Thai" + "\n" + \
                         "╠❂ tr : Turkish" + "\n" + \
                         "╠❂ uk : Ukrainian" + "\n" + \
                         "╠❂ vi : Vietnamese" + "\n" + \
                         "╠❂ cy : Welsh" + "\n" + \
                         "╚══════════════┛" + "\n" + "\n\n" + \
                          "「Contoh : say-id Pengen Anu」"
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange = "╔══════════════┓" + "\n" + \
                       "╠⌬ ✰self protect✰    ⌬" + "\n" + \
                       "╚══════════════┛" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "          ʜᴇʟᴘ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "╔══════════════┓" + "\n" + \
                       "╠❂ af : afrikaans" + "\n" + \
                       "╠❂ sq : albanian" + "\n" + \
                       "╠❂ am : amharic" + "\n" + \
                       "╠❂ ar : arabic" + "\n" + \
                       "╠❂ hy : armenian" + "\n" + \
                       "╠❂ az : azerbaijani" + "\n" + \
                       "╠❂ eu : basque" + "\n" + \
                       "╠❂ be : belarusian" + "\n" + \
                       "╠❂ bn : bengali" + "\n" + \
                       "╠❂ bs : bosnian" + "\n" + \
                       "╠❂ bg : bulgarian" + "\n" + \
                       "╠❂ ca : catalan" + "\n" + \
                       "╠❂ ceb : cebuano" + "\n" + \
                       "╠❂ ny : chichewa" + "\n" + \
                       "╠❂ zh-cn : chinese (simplified)" + "\n" + \
                       "╠❂ zh-tw : chinese (traditional)" + "\n" + \
                       "╠❂ co : corsican" + "\n" + \
                       "╠❂ hr : croatian" + "\n" + \
                       "╠❂ cs : czech" + "\n" + \
                       "╠❂ da : danish" + "\n" + \
                       "╠❂ nl : dutch" + "\n" + \
                       "╠❂ en : english" + "\n" + \
                       "╠❂ eo : esperanto" + "\n" + \
                       "╠❂ et : estonian" + "\n" + \
                       "╠❂ tl : filipino" + "\n" + \
                       "╠❂ fi : finnish" + "\n" + \
                       "╠❂ fr : french" + "\n" + \
                       "╠❂ fy : frisian" + "\n" + \
                       "╠❂ gl : galician" + "\n" + \
                       "╠❂ ka : georgian" + "\n" + \
                       "╠❂ de : german" + "\n" + \
                       "╠❂ el : greek" + "\n" + \
                       "╠❂ gu : gujarati" + "\n" + \
                       "╠❂ ht : haitian creole" + "\n" + \
                       "╠❂ ha : hausa" + "\n" + \
                       "╠❂ haw : hawaiian" + "\n" + \
                       "╠❂ iw : hebrew" + "\n" + \
                       "╠❂ hi : hindi" + "\n" + \
                       "╠❂ hmn : hmong" + "\n" + \
                       "╠❂ hu : hungarian" + "\n" + \
                       "╠❂ is : icelandic" + "\n" + \
                       "╠❂ ig : igbo" + "\n" + \
                       "╠❂ id : indonesian" + "\n" + \
                       "╠❂ ga : irish" + "\n" + \
                       "╠❂ it : italian" + "\n" + \
                       "╠❂ ja : japanese" + "\n" + \
                       "╠❂ jw : javanese" + "\n" + \
                       "╠❂ kn : kannada" + "\n" + \
                       "╠❂ kk : kazakh" + "\n" + \
                       "╠❂ km : khmer" + "\n" + \
                       "╠❂ ko : korean" + "\n" + \
                       "╠❂ ku : kurdish (kurmanji)" + "\n" + \
                       "╠❂ ky : kyrgyz" + "\n" + \
                       "╠❂ lo : lao" + "\n" + \
                       "╠❂ la : latin" + "\n" + \
                       "╠❂ lv : latvian" + "\n" + \
                       "╠❂ lt : lithuanian" + "\n" + \
                       "╠❂ lb : luxembourgish" + "\n" + \
                       "╠❂ mk : macedonian" + "\n" + \
                       "╠❂ mg : malagasy" + "\n" + \
                       "╠❂ ms : malay" + "\n" + \
                       "╠❂ ml : malayalam" + "\n" + \
                       "╠❂ mt : maltese" + "\n" + \
                       "╠❂ mi : maori" + "\n" + \
                       "╠❂ mr : marathi" + "\n" + \
                       "╠❂ mn : mongolian" + "\n" + \
                       "╠❂ my : myanmar (burmese)" + "\n" + \
                       "╠❂ ne : nepali" + "\n" + \
                       "╠❂ no : norwegian" + "\n" + \
                       "╠❂ ps : pashto" + "\n" + \
                       "╠❂ fa : persian" + "\n" + \
                       "╠❂ pl : polish" + "\n" + \
                       "╠❂ pt : portuguese" + "\n" + \
                       "╠❂ pa : punjabi" + "\n" + \
                       "╠❂ ro : romanian" + "\n" + \
                       "╠❂ ru : russian" + "\n" + \
                       "╠❂ sm : samoan" + "\n" + \
                       "╠❂ gd : scots gaelic" + "\n" + \
                       "╠❂ sr : serbian" + "\n" + \
                       "╠❂ st : sesotho" + "\n" + \
                       "╠❂ sn : shona" + "\n" + \
                       "╠❂ sd : sindhi" + "\n" + \
                       "╠❂ si : sinhala" + "\n" + \
                       "╠❂ sk : slovak" + "\n" + \
                       "╠❂ sl : slovenian" + "\n" + \
                       "╠❂ so : somali" + "\n" + \
                       "╠❂ es : spanish" + "\n" + \
                       "╠❂ su : sundanese" + "\n" + \
                       "╠❂ sw : swahili" + "\n" + \
                       "╠❂ sv : swedish" + "\n" + \
                       "╠❂ tg : tajik" + "\n" + \
                       "╠❂ ta : tamil" + "\n" + \
                       "╠❂ te : telugu" + "\n" + \
                       "╠❂ th : thai" + "\n" + \
                       "╠❂ tr : turkish" + "\n" + \
                       "╠❂ uk : ukrainian" + "\n" + \
                       "╠❂ ur : urdu" + "\n" + \
                       "╠❂ uz : uzbek" + "\n" + \
                       "╠❂ vi : vietnamese" + "\n" + \
                       "╠❂ cy : welsh" + "\n" + \
                       "╠❂ xh : xhosa" + "\n" + \
                       "╠❂ yi : yiddish" + "\n" + \
                       "╠❂ yo : yoruba" + "\n" + \
                       "╠❂ zu : zulu" + "\n" + \
                       "╠❂ fil : Filipino" + "\n" + \
                       "╠❂ he : Hebrew" + "\n" + \
                       "╚══════════════┛" + "\n" + "\n\n" + \
                       "「Contoh : tr-id Pengen Anu」"
    return helpLanguange
#==============================================================================#
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                gye.blockContact(op.param1)           
        if op.type == 13:
            if gyeMID in op.param3:
                G = gye.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            gye.rejectGroupInvitation(op.param1)
                        else:
                            gye.acceptGroupInvitation(op.param1)
                    else:
                        gye.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        gye.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    gye.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
#        if op.type == 24:
#            if settings["autoLeave"] == True:
#                line.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".say " in msg.text.lower():
                    spl = re.split(".say ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'my help':
                    myHelp = myhelp()
                    gye.sendMessage(to, str(myHelp))
                elif text.lower() == 'help set':
                    helpSet = helpset()
                    gye.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'help kicker':
                    helpKicker = helpkicker()
                    gye.sendMessage(to, str(helpKicker))
                elif text.lower() == 'help group':
                    listGrup = listgrup()
                    gye.sendMessage(to, str(listGrup))
                elif text.lower() == 'help setting':
                    helpSetting = helpsetting()
                    gye.sendMessage(to, str(helpSetting))
                elif text.lower() == 'help media':
                    socMedia = socmedia()
                    gye.sendMessage(to, str(socMedia))
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    gye.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'languange':
                    helpLanguange = helplanguange()
                    gye.sendMessage(to, str(helpLanguange))
#==============================ถึงนี่เเล้ว================================================#
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] GYEVHA BOTS TIGA")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    gye.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    gye.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    gye.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    gye.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")						
                elif text.lower() == 'รีบอท':
                    gye.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    gye.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u104e95aaefb53cf411f77353f6a96ece"
                        creator = gye.getContact(owner)
                        contact = gye.getContact(gyeMID)
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╔══[ ✯ɢʜᴏsᴛ ᴛᴇᴀᴍ✯ ]"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ]"
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ✯ɢʜᴏsᴛ ᴛᴇᴀᴍ✯ ]"
                        gye.sendContact(to, owner)
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#==============================================================================#
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔════[ Status ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠ รับแอดออโต้ ✔"
                        else: ret_ += "\n╠ รับแอดออโต้    ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ เข้าห้องออโต้    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ยกเลิกเชิญกลุ่มเมื่อมีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ยกเลิกเชิญกลุ่ม    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ออกแชทรวม ✔"
                        else: ret_ += "\n╠ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ อ่านออโต้ ✔"
                        else: ret_ += "\n╠ อ่านออโต้   ✘ "				
                        if settings["checkSticker"] == True: ret_ += "\n╠ Sticker ✔"
                        else: ret_ += "\n╠ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ แสดงภาพคนแทค ✘ "						
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ กันเชิญ ✔"
                        else: ret_ += "\n╠ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ กันยกเชิญ ✔"
                        else: ret_ += "\n╠ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ป้องกัน ✔"
                        else: ret_ += "\n╠ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✘ "						
                        ret_ += "\n╚════[ Status ]═════┛"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "Autoadd enabled.")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "Autoadd disabled.")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "Autojoin enabled.")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "Auto Join disabled.")
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    gye.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    gye.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    gye.sendText(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    gye.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                gye.sendText(msg.to,"Value is wrong")
                        else:
                                gye.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "Autoleave enabled.")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "Autoleave disabled.")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "Autoread message enabled.")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "Autoread message disabled.")
                elif text.lower() == 'sticker on':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "Check sticker enabled.")
                elif text.lower() == 'sticker off':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "Check sticker disabled.")                
#==============================================================================#                                     
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = gye.getGroup(to)
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                    gye.sendMessage(to, "Itu Pembuat Groupnya")
                elif text.lower() == 'groupid':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "Name Group -> \n" + gid.name)
                elif text.lower() == 'url':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "Link Qr to open")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Link Qr to open")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "Link Qr to closed.")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Link Qr to closed.")
                elif text.lower() == 'groupinfo':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))				
                elif ".invitetocall" == msg.text.lower():
                    gye.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    gye.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")	
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gye.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass	
                elif msg.text.lower() == ".getjoined":
                    gye.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = gye.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += gye.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            gye.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    gye.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".info " in msg.text.lower():
                    spl = re.split(".info ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = gye.getContact(uid)
                            try:
                                gye.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            gye.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            gye.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            gye.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            gye.sendMessage(msg)
                elif "|!" in msg.text:
                    spl = msg.text.split("|!")                    
                    if spl[len(spl)-1] == "":
                        gye.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)	
                elif ".denyall" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = gye.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        gye.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                gye.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    gye.sendText(gr,spl[1])
                                gye.leaveGroup(gr)
                            except:
                                pass
                        gye.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        gye.sendMessage(msg)
                elif ".remove " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            gye.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        gye.findAndAddContactsByMids(allmid)
                        gye.inviteIntoGroup(msg.to,allmid)
                        gye.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == ".myid":
                    gye.sendText(msg.to,user1)
                elif ".tx " in msg.text.lower():
                    spl = re.split(".tx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        gye.kedapkedip(msg.to,spl[1])
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        gye.updateProfile(prof)
                        gye.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        gye.updateProfile(prof)
                        gye.sendText(msg.to,"สำเร็จแล้ว")
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            gye.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            gye.sendText(msg.to,str(e))	
                elif msg.text.lower().startswith(".ctt "):
                    try:
                        text = msg.text.split(" ",1)[1]
                        headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                        }
                        data = {
                        "q":text
                        }
                        conv = BeautifulSoup(requests.post("http://lullar-de-2.appspot.com/",headers=headers,data=data).content,"html.parser").find("span",attrs={"style":"font-size:40px"}).text
                        if msg.toType != 0:
                                gye.sendText(msg.to,"Conversion:\n"+conv)
                        else:
                                gye.sendText(msg.from_,"Conversion:\n"+conv)
                    except Exception as e:
                        print(e)						
                elif msg.text.lower().startswith("pz:gac "):
                    pnum = re.split("pz:gac ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                gye.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                gye.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                gye.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                gye.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                gye.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                gye.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        gye.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        gye.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gye.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            gye.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")				
#========================================ถึงนี้======================================#

#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    
                elif msg.text.lower().startswith("ownerdel "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                        if Owner == []:
                            gye.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠PHANTOM GHOST\n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 https://line.me/ti/p/_SnII2cQTs 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Added Target Fail !")
                                break
                    
                elif msg.text.lower().startswith("admindel "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
              #      else:
               #         gye.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                #    if msg._from in Owner:
                        if admin == []:
                            gye.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠PHANTOM GHOST\n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 https://line.me/ti/p/_SnII2cQTs  〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To On")
                                
                elif text.lower() == 'protect off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == '*เปิดป้องกัน':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["join link"] = True
                        gye.sendMessage(msg.to,"Join link on")
                        gye.sendMessage(msg.to,"Qrprotect on")
                        gye.sendMessage(msg.to,"Protect on")
                        gye.sendMessage(msg.to,"Inviteprotect on")
                        gye.sendMessage(msg.to,"Cancelprotect on")
                        gye.sendMessage(msg.to,"➲ All Protect Set To On")
                        		            
                elif text.lower() == '*ปิดป้องกัน':
             #       if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        gye.sendMessage(msg.to,"Qrprotect Off")
                        gye.sendMessage(msg.to,"Protect Off")
                        gye.sendMessage(msg.to,"Inviteprotect Off")
                        gye.sendMessage(msg.to,"Cancelprotect Off")
                        gye.sendMessage(msg.to,"➲ All Protect Set To Modar")
            #        else:
             #           gye.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------               
                                                                                        
#==============================================================================#
                elif msg.text.lower() == 'โชว์':
                        gye.sendContact(to, gyeMID)
                        ais.sendContact(to, aisMID)
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                elif text.lower() in ["*หนีหำ"]:    
                    #gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                elif text.lower() in ["*ลาก่อน"]:    
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)      
                elif text.lower() in ["*มาหำ"]:    
                    G = gye.getGroup(msg.to)
                    ginfo = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    gye.updateGroup(G)
                    invsend = 0
                    Ticket = gye.reissueGroupTicket(msg.to)
                    ais.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    gye.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    gye.updateGroup(G)
                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
                    gye.sendMessage(msg.to,"➲ คนนี้ไง น่ารัก อย่า แอดมามั่วล่ะ เดียวจะหลงรัก")
                elif text.lower() == 'mymid':
                    gye.sendMessage(msg.to,"[MID]\n" +  gyeMID)
                elif text.lower() == 'myname':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            mi_d = contact.mid
                            gye.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("midnya "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = gye.getProfileCoverURL(ls)
                                gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            gye.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        gye.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = gye.getGroup(to)
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'gt':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'เปิดห้อง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'ปิดห้อง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                        settings["blacklist"] = {}
                        gye.sendMessage(msg.to,"➲ Done")
                        ais.sendMessage(msg.to,"➲ Done")
                        ki2.sendMessage(msg.to,"➲ Done")
                        ki3.sendMessage(msg.to,"➲ Done")
                        ki4.sendMessage(msg.to,"➲ Done")
                        ais.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki2.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki3.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki4.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki4.sendMessage(msg.to,"➲ Jangan Jadi Penjahat yah kakak Agar Tak Masuk Blaclist ku")
                        
                elif text.lower() == 'absen':
                        gye.sendMessage(msg.to,"➲ Gye 1")
                        ais.sendMessage(msg.to,"➲ Gye 2")
                        ki2.sendMessage(msg.to,"➲ Gye 3")
                        ki3.sendMessage(msg.to,"➲ Gye 4")
                        ki4.sendMessage(msg.to,"➲ Gye 5")
                        gye.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                        
                elif text.lower() == 'bancontact':
                        settings["wblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                        if settings["blacklist"] == {}:
                            gye.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            gye.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, gye.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            gye.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("บาย "):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ciak all member':
                 #   if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            #gs = gye.getGroup(msg.to)
                            gs = ais.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
                           #gye.sendMessage(msg.to,"「 Bye All 」")
                           #gye.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ais,ki2,ki3,ki4]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    gye.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'แท็ก':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        gye.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        gye.sendMessage(to, "จำนวนสมาชิคทั้งหมด {} คน".format(str(len(nama))))          
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                gye.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            gye.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            gye.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        gye.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        gye.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        gye.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        gye.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            gye.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = gye.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            gye.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        gye.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#   
                elif "Broadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbroadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif "Film:" in msg.text:
                    proses = msg.text.split(":")
                    get = msg.text.replace(proses[0] + ":","")
                    getfilm = get.split()
                    title = getfilm[0]
                    tahun = getfilm[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = time.time()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    line.sendImageWithURL(msg.to, str(path))
                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
		elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
			ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ จำนวน Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "fotoig" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
			end_cursor = ''
                        for count in range(1):
                            print(('send foto : ', count))
                            r = x.get(profile, params={'max_id': end_cursor})                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                print((node['display_src']))
                                line.sendImageWithURL(msg.to,node['display_src'])
                elif "image" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
		elif "image" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "anime" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
				elif "youtube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผมการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
			elif msg.text in ["Cctv on"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Cctv on Ready")
                elif msg.text in ["Cctv off"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "Cctv Already Off")

                elif text.lower() == 'selfbot off':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)

                elif text.lower() == 'friendlist':
                    contactlist = line.getAllContactIds()
                    kontak = line
                    msgs="🎎List Friend🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎List Friend🎎\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["Blocklist"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════Daftar Akun Yang di Blocked═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["Friendlist mid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════List FriendMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
			
			elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "Pornhub":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text.lower() == 'invite:gcreator':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/uninstall"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass

                elif msg.text in ["Tagimage on","Tag2 on"]:
                        settings['potoMention'] = True
                        line.sendMessage(msg.to,"Respon enabled.")
                
                elif msg.text in ["Tagimage off","Tag2 off"]:
                        settings['potoMention'] = False
                        line.sendMessage(msg.to,"Respon disabled.")

                elif msg.text in ["Respontag on","Tag on","My respon on","Respon:on"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"AutoRespon enabled.")
                
                elif msg.text in ["Respontag off","Tag off","My respon off","Respon:off"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"Autorespon disabled.")

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["Inviteuser"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".invitecancel2":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
#==============================================================================#   
                elif "Broadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbroadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))
                        
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] GYEVHA BOTS KICK")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki2MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki3MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki4MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID gyeMID]
                if op.param3 in aisMID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID gyeMID]
                if op.param3 in ki2MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID gyeMID]
                if op.param3 in ki3MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID gyeMID]
                if op.param3 in ki4MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ais.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ais.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    gye.sendMessage(op.param1,"Jangan Buka Qr")
            else:
                gye.sendMessage(op.param1,"")
#==============================================================================#
       # if op.type == 55:
        #    print ("[ 55 ] GYEVHA BOTS EMPAT")
         #   if op.param1 in read["readPoint"]:
          #      _name = gye.getContact(op.param2).displayName
           #     tz = pytz.timezone("Asia/Jakarta")
           #     timeNow = datetime.now(tz=tz)
            #    timeHours = datetime.strftime(timeNow," (%H:%M)")
             #   read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
     #   backupData()
    #except Exception as error:
     #   logError(error)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["join ticket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = gye.findGroupByTicket(ticket_id)
                        gye.acceptGroupInvitationByTicket(group.id,ticket_id)
                        gye.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
