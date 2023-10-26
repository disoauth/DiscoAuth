from typing import List, Optional, Union

import requests

from .common import generate_token, getToken, htmlEncode, joinUrl

from .models import UserObj as uObj

apiUrl = "https://discord.com/api"


class AuthUrl:
    def __init__(self,
                 client_id: str,
                 scope: List[str],
                 redirect_uri: str) -> None:
        """
        Makes and returns a url that is used to authorize users

        :param client_id: The client ID of your discord app
        :param scope: A list of scopes you want to use
        :param redirect_uri: The redirect uri you want to use
        :type client_id: str
        :type scope: List[str]
        :type redirect_uri: str
        """
        self._client_id = client_id
        self._scope = scope
        self._redirect_uri = redirect_uri

    async def makeUrl(self) -> str:
        """
        Returns the authorization link that was made

        :async:
        :returns: The authorization link. Redirect the user to the link and after they authorize, they will return to your redirect URI.
        :rtype: str
        """
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


    class User:
        def __init__(self, access_token):
            self.access_token = access_token

        

        async def get_current_user(self):
            url = apiUrl + "/users/@me"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            r = requests.get(url, headers=headers)
            j = r.json()
            return uObj(j)

        async def get_user_guilds(self):
            url = apiUrl + "/users/@me/guilds"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            r = requests.get(url, headers=headers)
            return r.json()
            

