from typing import List

from .common import generate_token


class AuthUrl:
    """"""

    def __init__(self, client_id: str,
                 scope: List[str],
                 redirect_uri: str) -> None:

        self.bUrl = "https://discord.com/oauth2/authorize?response_type=code&"
        self.client_id = "client_id=" + client_id + "&"
        x = 0
        strScope = ""
        while x < len(scope):
            strScope = strScope + scope[x] + "%20"
        x += 1
        self.scope = "scope=" + strScope[:-3]
        redRep1 = redirect_uri.replace(":", "%3A")
        redRep2 = redRep1.replace("/", "%2F")
        redRep3 = redRep2.replace("-", "%2D")
        self.redirect_uri = "redirect_uri=" + redRep3
        self.state = "state=" + generate_token()
        self.url = (self.bUrl
                    + self.client_id
                    + self.redirect_uri
                    + "&"
                    + self.scope
                    + "&"
                    + self.state)

    def __str__(self) -> str:
        return self.url
