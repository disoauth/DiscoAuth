import json
from random import SystemRandom
from typing import List

import requests

_UNICODE_ASCII_CHARACTER_SET = ('a',
                                'b',
                                'c',
                                'd',
                                'e',
                                'f',
                                'g',
                                'h',
                                'i',
                                'j',
                                'k',
                                'l',
                                'm',
                                'n',
                                'o',
                                'p',
                                'q',
                                'r',
                                's',
                                't',
                                'u',
                                'v',
                                'w',
                                'x',
                                'y',
                                'z',
                                'A',
                                'B',
                                'C',
                                'D',
                                'E',
                                'F',
                                'G',
                                'H',
                                'I',
                                'J',
                                'K',
                                'L',
                                'M',
                                'N',
                                'O',
                                'P',
                                'Q',
                                'R',
                                'S',
                                'T',
                                'U',
                                'V',
                                'W',
                                'X',
                                'Y',
                                'Z',
                                '0',
                                '1',
                                '2',
                                '3',
                                '4',
                                '5',
                                '6',
                                '7',
                                '8',
                                '9')


async def generate_token(length=30, chars=_UNICODE_ASCII_CHARACTER_SET):
    rand = SystemRandom()
    return ''.join(rand.choice(chars) for x in range(length))


async def getToken(code: str,
             scope: list[str],
             redirect_uri: str,
             client_id: str,
             client_secret: str) -> dict[str, str]:
    url = "https://discord.com/api/oauth2/token"
    scopeStr = " ".join(scope)
    rDict: dict[str, str] = {"error": "nothing loaded"}
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url=url,
                      data=data,
                      headers=headers)
    return r.json()  # returns the json file

async def joinUrl(clientID: str, scopes: str, redirectUri: str, state: str) -> str:
    baseUrl = "https://discord.com/oauth2/authorize?"
    urlList = [baseUrl,
               "response_type=code",
               "&",
               "client_id=",
               clientID,
               "&",
               "scope=",
               scopes,
               "&",
               "state=",
               state,
               "&",
               "redirect_uri=",
               redirectUri]
    url = "".join(urlList)
    return url

bot_perms = {
  'CREATE_INSTANT_INVITE': 0x1,
  'KICK_MEMBERS': 0x2,
  'BAN_MEMBERS': 0x4,
  'ADMINISTRATOR': 0x8,
  'MANAGE_CHANNELS': 0x10,
  'MANAGE_GUILD': 0x20,
  'ADD_REACTIONS': 0x40,
  'VIEW_AUDIT_LOG': 0x80,
  'PRIORITY_SPEAKER': 0x100,
  'STREAM': 0x200,
  'VIEW_CHANNEL': 0x400,
  'SEND_MESSAGES': 0x800,
  'SEND_TTS_MESSAGES': 0x1000,
  'MANAGE_MESSAGES': 0x2000,
  'EMBED_LINKS': 0x4000,
  'ATTACH_FILES': 0x8000,
  'READ_MESSAGE_HISTORY': 0x10000,
  'MENTION_EVERYONE': 0x20000,
  'USE_EXTERNAL_EMOJIS': 0x40000,
  'VIEW_GUILD_INSIGHTS': 0x80000,
  'CONNECT': 0x100000,
  'SPEAK': 0x200000,
  'MUTE_MEMBERS': 0x400000,
  'DEAFEN_MEMBERS': 0x800000,
  'MOVE_MEMBERS': 0x1000000,
  'USE_VAD': 0x2000000,
  'CHANGE_NICKNAME': 0x4000000,
  'MANAGE_NICKNAMES': 0x8000000,
  'MANAGE_ROLES': 0x10000000,
  'MANAGE_WEBHOOKS': 0x20000000,
  'MANAGE_GUILD_EXPRESSIONS': 0x40000000,
  'USE_APPLICATION_COMMANDS': 0x80000000,
  'REQUEST_TO_SPEAK': 0x100000000,
  'MANAGE_EVENTS': 0x200000000,
  'MANAGE_THREADS': 0x400000000,
  'CREATE_PUBLIC_THREADS': 0x800000000,
  'CREATE_PRIVATE_THREADS': 0x1000000000,
  'USE_EXTERNAL_STICKER': 0x2000000000,
  'SEND_MESSAGES_IN_THREADS': 0x4000000000,
  'USE_EMBEDDED_ACTIVITIES': 0x8000000000,
  'MODERATE_MEMBERS': 0x10000000000,
  'VIEW_CREATOR_MONETIZATION_ANALYTICS': 0x20000000000,
  'USE_SOUNDBOARD': 0x40000000000,
  'USE_EXTERNAL_SOUNDS': 0x200000000000,
  'SEND_VOICE_MESSAGES': 0x400000000000
}

bot_perms_key = {
      0:'CREATE_INSTANT_INVITE',
      1:'KICK_MEMBERS',
      2:'BAN_MEMBERS',
      3:'ADMINISTRATOR',
      4:'MANAGE_CHANNELS',
      5:'MANAGE_GUILD',
      6:'ADD_REACTIONS',
      7:'VIEW_AUDIT_LOG',
      8:'PRIORITY_SPEAKER',
      9:'STREAM',
      10:'VIEW_CHANNEL',
      11:'SEND_MESSAGES',
      12:'SEND_TTS_MESSAGES',
      13:'MANAGE_MESSAGES',
      14:'EMBED_LINKS',
      15:'ATTACH_FILES',
      16:'READ_MESSAGE_HISTORY',
      17:'MENTION_EVERYONE',
      18:'USE_EXTERNAL_EMOJIS',
      19:'VIEW_GUILD_INSIGHTS',
      20:'CONNECT',
      21:'SPEAK',
      22:'MUTE_MEMBERS',
      23:'DEAFEN_MEMBERS',
      24:'MOVE_MEMBERS',
      25:'USE_VAD',
      26:'CHANGE_NICKNAME',
      27:'MANAGE_NICKNAMES',
      28:'MANAGE_ROLES',
      29:'MANAGE_WEBHOOKS',
      30:'MANAGE_GUILD_EXPRESSIONS',
      31:'USE_APPLICATION_COMMANDS',
      32:'REQUEST_TO_SPEAK',
      33:'MANAGE_EVENTS',
      34:'MANAGE_THREADS',
      35:'CREATE_PUBLIC_THREADS',
      36:'CREATE_PRIVATE_THREADS',
      37:'USE_EXTERNAL_STICKER',
      38:'SEND_MESSAGES_IN_THREADS',
      39:'USE_EMBEDDED_ACTIVITIES',
      40:'MODERATE_MEMBERS',
      41:'VIEW_CREATOR_MONETIZATION_ANALYTICS',
      42:'USE_SOUNDBOARD',
      45:'USE_EXTERNAL_SOUNDS',
      46:'SEND_VOICE_MESSAGES'
}

async def permsByList(perm_list: List[int]) -> int:
    perms = 0x0
    for perm in perm_list:
        perms |= bot_perms[bot_perms_key[perm]]
    return perms

async def htmlEncode(str):
    str1 = str.replace(" ", "%20")
    str2 = str1.replace(":", "%3A")
    str3 = str2.replace("/", "%2F")
    return str3
