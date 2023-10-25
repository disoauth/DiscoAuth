from typing import List, Optional, Union

import requests

from .common import generate_token, getToken, htmlEncode, joinUrl

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
            return UserObj(j['id'],
                           j['username'],
                           j['discriminator'], 
                           j['global_name'],
                           j['avatar'],
                           j['bot'],
                           j['system'],
                           j['mfa_enabled'],
                           j['banner'],
                           j['accent_color'],
                           j['locale'],
                           j['verified'],
                           j['email'],
                           j['flags'],
                           j['premium_type'],
                           j['public_flags'],
                           j['avatar_decoration'])

        async def get_user_guilds(self):
            url = apiUrl + "/users/@me/guilds"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            r = requests.get(url, headers=headers)
            return r.json()
            
class UserObj:
            def __init__(self,
                         id,
                         username: str,
                         discriminator: str,
                         global_name: str | None = None,
                         avatar: str | None = None,
                         bot: bool | None = None,
                         system: bool | None = None,
                         mfa_enabled: bool | None = None,
                         banner: str | None = None,
                         accent_color: int | None = None,
                         locale: str | None = None,
                         verified: bool | None = None,
                         email: str | None = None,
                         flags: int | None = None,
                         premium_type: int | None = None,
                         public_flags: int | None = None,
                         avatar_decoration: str | None = None) -> None:
                self.id = id
                self.username = username
                self.discriminator = discriminator
                if global_name is not None:
                    self.global_name = global_name
                if avatar is not None:
                    self.avatar = avatar
                if bot is not None:
                    self.bot = bot
                else:
                    self.bot = False
                if system is not None:
                    self.system = system
                else:
                    self.system = False
                self.mfa_enabled = mfa_enabled
                self.banner = banner
                self.accent_color = accent_color
                self.locale = locale
                if verified is not None:
                    self.verified = verified
                else:
                    self.verified = None
                if email is not None:
                    self.email = email
                else:
                    self.email = None
                self.flags = flags
                self.premium_type = premium_type
                self.public_flags = public_flags
                self.avatar_decoration = avatar_decoration
