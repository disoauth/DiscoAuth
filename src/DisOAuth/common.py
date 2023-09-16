import json
from secrets import SystemRandom

import requests

_UNICODE_ASCII_CHARACTER_SET = ('abcdefghijklmnopqrstuvwxyz',
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                '0123456789')


def generate_token(length=30, chars=_UNICODE_ASCII_CHARACTER_SET):
    _rand = SystemRandom()
    return ''.join(_rand.choice(chars) for x in range(length))


def getToken(code: str,
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
        'redirect_uri': redirect_uri,
        'scope': scopeStr
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url=url,
                      data=data,
                      headers=headers,
                      auth=(client_id, client_secret))
    if r.status_code == 200:
        rDict = json.loads(str(r.json))
    return rDict  # returns the json file
