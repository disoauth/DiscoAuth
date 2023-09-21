import json
from typing import List

import requests

from .common import generate_token, getToken, htmlEncode, joinUrl

apiUrl = "https://discord.com/api"


class AuthUrl:
    def __init__(self,
                 client_id: str,
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

    async def makeUrl(self) -> str:
        scope = self._scope
        redirect_uri = self._redirect_uri
        client_id = self._client_id
        state = await generate_token()
        x = 0
        strScope = ""
        while x < len(scope):
            strScope = strScope.join(f"{scope[x]} ")
            x += 1
        _strScope = strScope[:-1]
        _scope = _strScope.replace(" ", "%20")
        redirectUri = await htmlEncode(redirect_uri)
        url = await joinUrl(client_id, _scope, redirectUri, state)
        return url


class discordApi:

    def __init__(self,
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
