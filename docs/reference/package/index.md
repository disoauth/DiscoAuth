# Package Reference

Remember that everything *must* be `await`-ed

​

## Class AuthUrl
`class AuthUrl(self, client_id: str, scope: List[str], redirect_uri: str) -> None`

Makes and returns that is used to authorize users

Arguments:
- client_id: The client ID of your application
- scope: A list of strings of the scopes you want touse
- redirect_uri: the redirect uri you want to use

​

**Function makeUrl**

`async def makeUrl(self) -> str`

A function that is part of the AuthUrl class, that returns the authorization link that was made. Must be `await`-ed

Returns:
A string, to be used to authorize a Discord User and get a code


​



## Class discordApi
`class discordApi(self, client_id: str, client_secret: str, scope: List[str], redirect_uri: str) -> None`

Where you can get an access code, and use some of Discord's api links

​

**Function Access Token**

`async def accessToken(self, code: str) -> dict[str, str]`

Takes values input into discordApi, and the code returns the response as a dictionary

P.S. This returns a dictionary, containing the entire response from Discord



Arguments:
- code: the code parameter from the query string


​


### Class User
A subclass of the discordApi class

`class User(self, access_token: str) -> dict[str, str]`

Arguments:
- access_token: The access token you would like to use

​

**Function get_current_user**
`async def get_current_user(self) -> dict`

returns a dictionary containing a full Discord User Object
