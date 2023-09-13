from typing import List

from .common import generate_token


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
