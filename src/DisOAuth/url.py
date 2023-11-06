from typing import List, Optional, Union, Type, Dict

import requests

from .common import generate_token, getToken, htmlEncode, joinUrl

from .models import UserObj as uObj, GuildObj as gObj

apiUrl = "https://discord.com/api"



class auth:
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
        self.strScope = ""
        for s in scope:
            self.strScope += s
            selg.strScope += " "
        scope1 = self.strScope.rstrip(" ")
        _scope = scope1.replace(" ", "%20")
        redirectUri = await htmlEncode(redirect_uri)
        url = await joinUrl(client_id, _scope, redirectUri, state)
        return url


class discord:
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

        

        async def get_current_user(self) -> uObj:
            url = apiUrl + "/users/@me"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            r = requests.get(url, headers=headers)
            j = r.json()
            return uObj(j)

        async def get_user_guilds(self,
                                  with_count: bool | None = False) -> List[gObj]:
            url = apiUrl + "/users/@me/guilds"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            query = {}
            if with_count == True:
                query['with_counts'] = True
            else:
                query['with_counts'] = False
            r = requests.get(url, headers=headers)
            guildList = []
            for guild in r.json():
                guildList.append(gObj(guild))
            return guildList

        async def get_guild(self,
                            id: int,
                            with_counts: bool | None = False) -> gObj:
            url = apiUrl + f"/guilds/{id}"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token
            }
            query = {}
            if with_counts == True:
                query['with_counts'] = True
            elif with_counts == False:
                query['with_counts'] = False
            r = requests.get(url, headers=headers, params=query)
            return gObj(r.json())

class bot:
    def __init__(self,
                 client_id,
                 permissions: int | Type[permissions]) -> None:
        """
        Makes an auth url for bots
        :param client_id: The client id of your bot
        :param permissions: The permissions of your bot. Either a number or a list of permissions
        :type client_id: int
        :type permissions: int or List[str] 
        """
        self.id = int(client_id)
        if permissions is Type[permissions]:
            self.permissions = permissions.value
        else:
            self.permissions = permissions

    async def url(self) -> str:
        """
        Returns the url for bot auth
        :return: The url for bot auth
        :rtype: str
        """
        url = f"https://discord.com/api/oauth2/authorize?client_id={self.id}&permissions={self.permissions}&scope=bot"
        return url

class permissions:
    def __init__(self, 
                 permissions: int | str | List[int | str] | Dict[int | str, bool] |None = None) -> None:
        """
        Updates, removes, or adds permissions that you want use

        :param permissions: The permissions you want to use. Optional, as you can update with methods
        :type permissions: List or int or None. When None, defaults to 0, or no permissions. When using int's, use the decimal version of the number.
        """
        self.perm_list = ["create_instant_invite",
                          "kick_members",
                          "ban_members",
                          "administrator",
                          "manage_channels",
                          "manage_guild",
                          "add_reactions",
                          "view_audit_log",
                          "priority_speaker",
                          "stream",
                          "view_channel",
                          "send_messages",
                          "send_tts_messages",
                          "manage_messages",
                          "embed_links",
                          "attach_files",
                          "read_message_history",
                          "mention_everyone",
                          "use_external_emojis",
                          "view_external_guilds",
                          "connect",
                          "speak",
                          "mute_members",
                          "deafen_members",
                          "move_members",
                          "use_vad",
                          "change_nickname",
                          "manage_nicknames",
                          "manage_roles",
                          "manage_webhooks",
                          "manage_guild_expressions",
                          "use_application_commands",
                          "request_to_speak",
                          "manage_events",
                          "manage_threads",
                          "create_public_threads",
                          "create_private_threads",
                          "use_external_sticker",
                          "send_messages_in_threads",
                          "use_embedded_activities",
                          "moderate_members",
                          "view_creator_monetization_analytics",
                          "use_soundboard",
                          "use_external_sounds",
                          "send_voice_message"]
        self.create_instant_invite = False
        self.kick_members = False
        self.ban_members = False
        self.administrator = False
        self.manage_channels = False
        self.manage_guild = False
        self.add_reactions = False
        self.view_audit_log = False
        self.priority_speaker = False
        self.stream = False
        self.view_channel = False
        self.send_messages = False
        self.send_tts_messages = False
        self.manage_messages = False
        self.embed_links = False
        self.attach_files = False
        self.read_message_history = False
        self.mention_everyone = False
        self.use_external_emojis = False
        self.view_guild_insights = False
        self.connect = False
        self.speak = False
        self.mute_members = False
        self.deafen_members = False
        self.move_members = False
        self.use_vad = False
        self.change_nickname = False
        self.manage_nicknames = False
        self.manage_roles = False
        self.manage_webhooks = False
        self.manage_guild_expressions = False
        self.use_application_commands = False
        self.request_to_speak = False
        self.manage_events = False
        self.manage_threads = False
        self.create_public_threads = False
        self.create_private_threads = False
        self.use_external_sticker = False
        self.send_messages_in_threads = False
        self.use_embedded_activities = False
        self.moderate_members = False
        self.view_creator_monetization_analytics = False
        self.use_soundboard = False
        self.use_external_sounds = False
        self.send_voice_messages = False
        
        self.value = 0x0

        if permissions is None:
            pass
        elif isinstance(permissions, List):
            for perm in permissions:
                if isinstance(perm, int):
                    if perm not in bot_perms_key:
                        raise ValueError(f"{perm} is not a valid permission")
                    self.value |= bot_perms[bot_perms_key[perm]]
                    if getattr(self, bot_perms_key[perm].lower()) is False:
                        setattr(self, bot_perms_key[perm].lower(), True)
                    if getattr(self, bot_perms_key[perm].lower()) is True:
                        setattr(self, bot_perms_key[perm].lower(), False)
                elif isinstance(perm, str):
                    if perm.upper() not in bot_perms:
                        raise ValueError(f"{perm} is not a valid permission")
                    else:
                        self.value |= bot_perms[perm.upper()]
                        if getattr(self, perm.lower()) is False:
                            setattr(self, perm.lower(), True)
                        if getattr(self, perm.lower()) is True:
                            setattr(self, perm.lower(), False)
        elif isinstance(permissions, int):
            if permissions == 43 or permissions == 44:
                raise ValueError("43 and 44 are not valid permission numbers")
            self.value |= bot_perms[bot_perms_key[permissions]]
            if getattr(self, bot_perms_key[permissions].lower()) is False:
                setattr(self, bot_perms_key[permissions].lower(), True)
            elif getattr(self, bot_perms_key[permissions].lower()) is True:
                setattr(self, bot_perms_key[permissions].lower(), False)
        elif isinstance(permissions, str):
            self.value |= bot_perms[permissions.upper()]
            if getattr(self, permissions.lower()) is False:
                setattr(self, permissions.lower(), True)
            elif getattr(self, permissions.lower()) is True:
                setattr(self, permissions.lower(), False)
        elif isinstance(permissions, dict):
            for num in list(permissions.keys()):
                if isinstance(num, int):
                    if permissions == 43 or permissions:
                        raise ValueError("43 and 44 are not valid permission numbers")
                    if num in bot_perms_key.keys():
                        if permissions[num] is True:
                            if (self.value & bot_perms[bot_perms_key[num]]) != bot_perms[bot_perms_key[num]]:
                                self.value |= bot_perms[bot_perms_key[num]]
                            setattr(self, bot_perms_key[int(num)].lower(), True)
                        elif permissions[num] is False:
                            if (self.value & bot_perms[bot_perms_key[num]]) == bot_perms[bot_perms_key[num]]:
                                self.value |= bot_perms[bot_perms_key[num]]
                            setattr(self, bot_perms_key[int(num)].lower(), False)
                        else:
                            raise ValueError("An unknown error occured")
                    if num not in bot_perms_key.keys():
                        raise ValueError(f"{num} is not a valid permission number")
                elif isinstance(num, str):
                    if num.upper() in bot_perms.values():
                        if permissions[num] is True:
                            if (self.value & bot_perms[num.upper()]) != bot_perms[num.upper()]:
                                self.value |= bot_perms[num.upper()]
                            setattr(self, num.lower(), True)
                        elif permissions[num] is False:
                            print(f"{permissions[num]} should be false")
                            if (self.value & bot_perms[num.upper()]) == bot_perms[num.upper()]:
                                self.value |= bot_perms[num.upper()]
                            setattr(self, num.lower(), False)
                        else:
                            raise ValueError(f"An unknown error occured")
                    elif num.upper() not in bot_perms.values():
                        raise ValueError(f"{permissions[num]} is not a valid permission")
                

    async def update(self,
                     permissions: List[str | int] | str | int | Dict[int | str, bool]) -> None:
        """
        Updates the permissions to update what permissions you want.
        If the permission is already added, updating will remove it, and vice versa
        
        :param permissions: The permissions you want to update
        :type permissions: List of int, List of str, int, or str"""
        if isinstance(permissions, List):
            for perm in permissions:
                if isinstance(perm, int):
                    if perm not in bot_perms_key:
                        raise ValueError(f"{perm} is not a valid permission")
                    self.value |= bot_perms[bot_perms_key[perm]]
                    if getattr(self, bot_perms_key[perm].lower()) is False:
                        setattr(self, bot_perms_key[perm].lower(), True)
                    if getattr(self, bot_perms_key[perm].lower()) is True:
                        setattr(self, bot_perms_key[perm].lower(), False)
                elif isinstance(perm, str):
                    if perm.upper() not in bot_perms:
                        raise ValueError(f"{perm} is not a valid permission")
                    else:
                        self.value |= bot_perms[perm.upper()]
                        if getattr(self, perm.lower()) is False:
                            setattr(self, perm.lower(), True)
                        if getattr(self, perm.lower()) is True:
                            setattr(self, perm.lower(), False)
        elif isinstance(permissions, int):
            if permissions == 43 or permissions == 44:
                raise ValueError("43 and 44 are not valid permission numbers")
            self.value |= bot_perms[bot_perms_key[permissions]]
            if getattr(self, bot_perms_key[permissions].lower()) is False:
                setattr(self, bot_perms_key[permissions].lower(), True)
            elif getattr(self, bot_perms_key[permissions].lower()) is True:
                setattr(self, bot_perms_key[permissions].lower(), False)
        elif isinstance(permissions, str):
            self.value |= bot_perms[permissions.upper()]
            if getattr(self, permissions.lower()) is False:
                setattr(self, permissions.lower(), True)
            elif getattr(self, permissions.lower()) is True:
                setattr(self, permissions.lower(), False)
        elif isinstance(permissions, dict):
            for num in list(permissions.keys()):
                if isinstance(num, int):
                    if permissions == 43 or permissions == 44:
                        raise ValueError("43 and 44 are not valid permission numbers")
                    if num in bot_perms_key:
                        if permissions[num] is True:
                            if (self.value & bot_perms[bot_perms_key[num]]) != bot_perms[bot_perms_key[num]]:
                                self.value |= bot_perms[bot_perms_key[num]]
                            setattr(self, bot_perms_key[int(num)].lower(), True)
                        elif permissions[num] is False:
                            if (self.value & bot_perms[bot_perms_key[num]]) == bot_perms[bot_perms_key[num]]:
                                self.value |= bot_perms[bot_perms_key[num]]
                            setattr(self, bot_perms_key[int(num)].lower(), False)
                        else:
                            raise ValueError("An unknown error occured")
                    if num not in bot_perms_key:
                        raise ValueError(f"{num} is not a valid permission number")
                elif isinstance(num, str):
                    if num.upper() in bot_perms:
                        if permissions[num] is True:
                            if (self.value & bot_perms[num.upper()]) != bot_perms[num.upper()]:
                                self.value |= bot_perms[num.upper()]
                            setattr(self, num.lower(), True)
                        elif permissions[num] is False:
                            print(f"{permissions[num]} should be false")
                            if (self.value & bot_perms[num.upper()]) == bot_perms[num.upper()]:
                                self.value |= bot_perms[num.upper()]
                            setattr(self, num.lower(), False)
                        else:
                            raise ValueError("An unknown error occured")
                    elif num.upper() not in bot_perms:
                        raise ValueError(f"{permissions[num]} is not a valid permission")

    async def add(self, 
                  permissions: int | str | List[int | str]) -> None:
        if isinstance(permissions, int):
            if permissions == 43 or permissions == 44:
                raise ValueError("43 and 44 are not valid permission numbers")
            if permissions in bot_perms_key.keys():
                setattr(self, bot_perms[bot_perms_key[permissions]].lower(), True)
                if (self.value & bot_perms[bot_perms_key[permissions]].upper()) != bot_perms[bot_perms_key[permissions]].upper():
                    self.value |= bot_perms[bot_perms_key[permissions]].upper()
            elif permissions not in bot_perms_key:
                raise ValueError(f"{permissions} is not a valid permission number. Use numbers 1 through 42, and 45 and 46")
            else:
                raise ValueError("An unknown error occured")
        elif isinstance(permissions, str):
            if permissions.upper() in bot_perms.keys():
                setattr(self, permissions.lower(), True)
                if (self.value & bot_perms[permissions.upper()]) != bot_perms[permissions.upper()]:
                    self.value |= bot_perms[permissions.upper()]
            elif permissions not in bot_perms:
                raise ValueError(f"{permissions} is not a valid permission.")
        elif isinstance(permissions, list):
            for perm in permissions:
                if isinstance(perm, int):
                    if perm == 43 or perm == 44:
                        raise ValueError("43 and 44 is not a valid permission number")
                    if perm in bot_perm_key:
                        pass
        else:
            raise ValueError("An unknown error occured")

    async def remove(self, 
                     permissions: int | str | List[int | str]) -> None:
        pass

    async def all(self) -> None:
        for perm in self.perm_list:
            setattr(self, perm, True)
            if getattr(self, perm) is False:
                self.value |= bot_perms[perm.upper()]

    async def none(self) -> None:
        for perm in self.perm_list:
            setattr(self, perm, False)
            if getattr(self, perm) is True:
                self.value &= bot_perms[perm.upper()]

    async def general(self) -> None:
        pass

    async def all_channel(self) -> None:
        pass

    async def membership(self) -> None:
        pass

    async def text(self) -> None:
        pass

    async def voice(self) -> None:
        pass

    async def stage(self) -> None:
        pass

    async def stage_moderator(self) -> None:
        pass

    async def elevated(self) -> None:
        pass

    async def events(self) -> None:
        pass

    async def advanced(self) -> None:
        pass

