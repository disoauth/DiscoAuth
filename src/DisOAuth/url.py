import json
from typing import List
import asyncio

import requests

from .common import generate_token, getToken

apiUrl = "https://discord.com/api"


class AuthUrl:
    def __init__(self, client_id: str,
                       scope: List[str],
                       redirect_uri: str) -> None:
        """Makes and returns a url that is used to authorize users

        Keyword arguments:
        client_id -- The client ID of your discord app
        scope -- A list of scopes you want to use
        redirect_uri -- The redirect uri you want to use
        """
        self._client_id = client_id
        self._scope = scope
        self._redirect_uri = redirect_uri

    async def makeUrl(self):
        genToken = asyncio.create_task(generate_token())
        state = await genToken
        x = 0
        strScope = ""
        while x < len(self._scope):
            strScope = strScope.join(f"{self._scope[x]} ")
            x += 1
        _strScope = strScope[:-1]
        scope = _strScope.replace(" ", "%20")
        encode = asyncio.create_task(htmlEncode(self._redirect_uri))
        redirectUri = await encode
        urlMake = asyncio.create_task(joinUrl(self._client_id, scope, redirectUri, state))
        url = await urlMake
        return url
        

class discordApi:

    async def __init__(self,
                       client_id,
                       client_secret,
                       scope: list[str],
                       redirect_uri) -> None:
        """Where you can get an access code, use the api links to get info

        client_id - The client id of your application
        client_secret - The client secret of your application
        scope - a list of the scopes you authorized for
        redirect_uri -- the redirect_uri you want to use
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.redirect_uri = redirect_uri

    async def accessToken(self, code) -> dict[str, str]:
        """Takes values input into discordApi, and the code
        returns the response as a dictionary

        Keyword Arguments:
        code -- The code you got when the user authorized
        """
        tokenDict = getToken(code,
                             self.scope,
                             self.redirect_uri,
                             self.client_id,
                             self.client_secret)
        return await tokenDict

    async def checkAuthInfo(self, token):
        """requests your auth info for your application, returning it as a dict

        If you want to get the full application object, use checkAppInfo()

        Keyword Arguments:
        token -- An access token, used for authorization"""
        url = apiUrl + "/oauth2/@me"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.get(url,
                         headers=headers,
                         auth=token)
        if r.status_code == 200:
            return json.loads(str(r.json))
