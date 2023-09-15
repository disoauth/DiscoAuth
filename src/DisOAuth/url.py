import json
from typing import List

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
        self._bUrl = "https://discord.com/oauth2/authorize?response_type=code&"
        self._client_id = "client_id=" + client_id + "&"
        _x = 0
        _strScope = ""
        while _x < len(scope):
            _strScope = _strScope + scope[_x] + "%20"
        _x += 1
        self._scope = "scope=" + _strScope[:-3]
        _redRep1 = redirect_uri.replace(":", "%3A")
        _redRep2 = _redRep1.replace("/", "%2F")
        _redRep3 = _redRep2.replace("-", "%2D")
        self._redirect_uri = "redirect_uri=" + _redRep3
        self._state = "state=" + generate_token()
        self.url = (self._bUrl
                    + self._client_id
                    + self._redirect_uri
                    + "&"
                    + self._scope
                    + "&"
                    + self._state)

    def __str__(self) -> str:
        return self.url


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

    def accessToken(self, code) -> dict[str, str]:
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
        return tokenDict

    def checkAuthInfo(self, token):
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
