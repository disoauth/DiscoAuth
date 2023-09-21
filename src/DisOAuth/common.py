import json
from random import SystemRandom

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
    return r.json  # returns the json file

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
    print(url)
    return url

async def htmlEncode(str):
    str1 = str.replace(" ", "%20")
    str2 = str1.replace(":", "%3A")
    str3 = str2.replace("/", "%2F")
    return str3
