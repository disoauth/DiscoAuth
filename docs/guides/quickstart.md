# Getting Started

Here, we will use the AuthUrl class to make an authorization url and the discordApi class to get user data

As always when learning, or even using a package, you have to import it. The async DisOAuth2 package can be imported using:
**`pip install Async-DisOAuth`**

Ok! Time to get your authorization url!

​
## Authorization Url

Before we even use the `import` statement, we need to set some variables to make the url, or at the very least know what you will put into the `AuthUrl` class

Since the `AuthUrl` class takes ***three*** arguments to work, you'll need to setup a `scope`, `client_id`, and a `redirect_uri` variable

There are some restrictions though, when it comes to `AuthUrl`. The one thing is that the `scope` argument only accepts a list of strings or `List[str,str]`

*Now* we can import everything we need for the authorization url

```
from DisOAuth import AuthUrl

client_id = "<Your app's client id>"
scope = ["identify", "email"]
redirect_uri = "<Your redirect uri (doesn't need to be html encoded before)>"

url = await AuthUrl(client_id, scope, redirect_uri).makeUrl()
```

And `url` would be your authorization url

Now, since I don't know what you will be using to get the query string, I am going to have to skip that part. Though, I do suggest using [quart's](https://quart.palletsprojects.com) `request.args.get` function, unless you are using flask

Since we have the code (after getting it from the query string), make sure to set it to a variable as we're gonna need it later. I'm gonna set it to `code`

​
## Access Token
I'm sure you already know this but, this part is really important. If you don't get it right, you won't be able to use **ANY** of discord's api links.

Since we need a different class to get the token, we will need to go back up and add the `discordApi` class to the import statement

`from DisOAuth import AuthUrl, discordApi`

If that doesn't work, import it using `from DisOAuth.url import discordApi`

***

To start, we need a new variable, the `client_secret`

using the other three variables and `client_secret` we can use:
```
api = discordApi(client_id, client_secret, scope, redirect_uri)
r = await api.accessToken(code)
token = r['access_token']
```
Now, `token` is your access token.

Remember, `discordApi.accessToken` returns a dictionary, containing the entire response, so you can still get the `refresh_token`

​
## User Object
Time to get that user data! I am proud to say, we don't need to import any other classes

You can use `r = await discordApi.User(token).get_current_user()` to get a response(`r`), which is a object-turned-dictionary, which is actually a Discord User Object

## The End... ?
Hooray! We can now get the user's avatar decoration hash! Or you know, the username

While this is the end of the user guide for this version (1.0.1), more will come out later

And if you can't wait, make sure to visit the API reference or the about pages
