# DiscordOAuth2
automatically follows through with the requests for Discord OAuth

[![Documentation Status](https://readthedocs.org/projects/async-disoauth2/badge/?version=latest)](https://async-disoauth2.readthedocs.io/en/latest/?badge=latest)

***

## Features
- Makes a Authorization Url automatically, using the client ID, redirect_uri, and the scopes you want
- Can get:
  - The access token
  - The user
  - The user's guilds

***

## What I'm working on for version 2.0.0

- [x] Get Guilds
  - Released in version 1.1
  - [x] Errors, will be fixed in version 1.4
    - Found error in the scope part of the url creation
- [ ] Models
  - [x] User Object
    - [x] Errors, fixed in version 1.3
  - [ ] Guild Object
- [ ] Bot OAuth
- [ ] Functioning CLI
