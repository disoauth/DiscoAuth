# DiscoAuth
automatically follows through with the requests for Discord OAuth

[![Documentation](https://img.shields.io/badge/docs-passing-light_green?style=for-the-badge&logo=readthedocs)](https://discoauth.rtfd.io)
[![Codecov](https://img.shields.io/codecov/c/gh/disoauth/DiscoAuth?style=for-the-badge&logo=codecov)](https://codecov.io/gh/disoauth/DiscoAuth)

***

## Features
- Makes a Authorization Url automatically, using the client ID, redirect_uri, and the scopes you want
- Can get:
  - The access token
  - The user
  - The user's guilds
  - A specific guild, using it's ID

It also makes bot auth url's

***

## What I'm working on for version 3.0.0

- [ ] Add functions and models for User and Guild
  - [ ] User
    - [ ] Functions
      - [ ] Get User
      - [ ] Modify Current User
      - [ ] Get Current Guild Members
      - [ ] Leave Guild
      - [ ] Create DM
      - [ ] Create Group DM
      - [ ] Get Current User Connections
      - [ ] Get Current User Application Role Connection
      - [ ] Update Current User Application Role Connection
  - [ ] Guild
    - [ ] Functions
      - [ ] Create Guild
      - [ ] Get Guild Preview
      - [ ] Modify Guild
      - [ ] Delete Guild
      - [ ] Get Guild Channels
      - [ ] Create Guild Channels
      - [ ] Modify Guild Channels Positions
      - [ ] List Active Guild Threads
      - [ ] Get Guild Member
      - [ ] List Guild Members
      - [ ] Search Guild Members
      - [ ] Add Guild Member
      - [ ] Modify Guild Member
      - [ ] Modify Current Member
      - [ ] Modify Current User Nick
      - [ ] Add Guild Member Role
      - [ ] Remove Guild Member Role
      - [ ] Remove Guild Member
      - [ ] Get Guild Bans
      - [ ] Get Guild Ban
      - [ ] Create Guild Ban
      - [ ] Remove Guild Ban
      - [ ] Get Guild Roles
      - [ ] Create Guild Role
      - [ ] Modify Guild Role Positions
      - [ ] Modify Guild Role
      - [ ] Modify Guild MFA Level
      - [ ] Delete Guild Role
      - [ ] Get Guild Prune Count
      - [ ] Begin Guild Prune
      - [ ] Get Guild Voice Regions
      - [ ] Get Guild Invites
      - [ ] Get Guild Integrations
      - [ ] Delete Guild Integration
      - [ ] Get Guild Widget Settings
      - [ ] Modify Guild Widget
      - [ ] Get Guild Widget
      - [ ] Get Guild Vanity URL
      - [ ] Get Guild Widget Image
      - [ ] Get Guild Welcome Screen
    - [ ] Models (Like channel, and role models)
- [ ] Raise `MissingScopes` when trying to use a functions that need extra scopes

***

### Useful Links:

- [License](https://github.com/disoauth/DiscoAuth/blob/main/LICENSE)
- [Contributing & Guidelines](https://github.com/disoauth/DiscoAuth/blob/main/CONTRIBUTING.md)
- [Roadmap](https://github.com/orgs/disoauth/projects/1)

***

## Coverage

[![Coverage](https://codecov.io/gh/disoauth/DiscoAuth/graphs/sunburst.svg?token=0A6DPREED2)](https://codecov.io/gh/disoauth/DiscoAuth)

***

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Arcader717"><img src="https://avatars.githubusercontent.com/u/134526462?v=4?s=100" width="100px;" alt="Arcader717"/><br /><sub><b>Arcader717</b></sub></a><br /><a href="#code-Arcader717" title="Code">💻</a> <a href="#doc-Arcader717" title="Documentation">📖</a> <a href="#example-Arcader717" title="Examples">💡</a> <a href="#tutorial-Arcader717" title="Tutorials">✅</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

***

## License

This project is under the [MIT License](https://en.wikipedia.org/wiki/MIT_License)
