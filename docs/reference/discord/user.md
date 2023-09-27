# User Discord API Reference
Contains all of the objects, and all of the usable links, that also link to any avaliable package functions

## Objects

### User Object
|Field|Type|Description|OAuth Scope|
|---|---|---|---|
|id|snowflake|the user's id|`identify`|
|username|string|the user's username (not unique)|`identify`|
|discriminator|string|the user's Discord-tag|`identify`|
|global_name|?string|The display name. For bots, it's the application name|`identify`|
|avatar|?string|the user's avatar hash|`identify`|
|bot?|boolean|Whether the user is a bot (application) or not|`identify`|
|system?|boolean|whether the user is a Discord System user or not|`identify`|
|mfa_enabled?|boolean|whether the user has two factor on or not|`identify`|
|banner?|?string|The user's banner hash|`identify`|
|accent_color?|?integer|The user's banner color, as a hexadecimal|`identify`|
|locale?|string|the user's chosen language option|`identify`|
|verified?|boolean|whther the email has been verified|`email`|
|email?|?string|the user's email|`email`|
|flags?|integer|the flags on the user's account|`identify`|
|premium_type?|integer|the type of nitro the user has|`identify`|
|public_flags?|integer|the public flags on the user's account|`identify`|
|avatar_decoration?|?string|the user's avatar decoration hash|`identify`|



## Links

**Get Current User**
> GET /users/@me
>
> Scopes: Identify (email if you want the response to include the user's email)

**Get User**
> GET /users/{user.id}
>
> Scopes: Identify (email if you want the response to include the user's email)
> 
> returns a user object for a given user ID

**Modify Current User**
> PATCH /user/@me
>
> Params:
>
> |Field|Type|Description|
> |---|---|---|
> |username|string| The user's username, if changed may cause the user's discriminator to be randomized|
> |avatar|?image data|if passed, modifies the user's avatar|

**Get Current User Guilds**
> GET /users/@me/guilds
>
> Scopes: guild
>
> Returns: List of Partial guild object
>
> Params:
>
> |Field|Type|Description|Required|Default|
> |---|---|---|---|---|
> |before|snowflake|gets guilds before this guild ID|false|absent|
> |after|snowflake|gets guilds after this guild ID|false|absent|
> |limit|integer|max number of guilds to return (1-200)|false|200|
> |with-counts|boolean|include approximate member and presence counts in response|false|false|

**Get Current User Guild Member**
> GET /users/@me/guilds/{guild.id}/member
>
> Scopes: `guilds.members.read`
>
> Returns a guild member object

**Leave Guild**
> DELETE /users/@me/guilds/{guild.id}
>
> Returns an empty 204 response on success

**Create DM**
> POST /users/@me/channels
>
> Should only be used when initiated by the user
>
> Params:
>
> |Field|Type|Description|
> |---|---|---|
> |recipient_id|snowflake|the recipient to open a DM channel with|

**Create Group DM**
> POST /users/@me/channels/
>
> Only 10 active group DM's are allowed at a time
>
> Scopes: `gdm.join`
> 
> Params:
>
> |Field|Type|Description|
> |---|---|---|
> |access_tokens|array of strings|access tokens of users that have granted your app the `gdm.join` scope|
> |nicks|dict|a dictionary of user ids to their respective nicknames|

**Get User Connections**
> GET /users/@me/connections
>
> Returns: A list of connection objects. Requires `connections` scope
>
> Scopes: `connections`

**Get User Application Role Connection**
> GET /users/@me/applications/{application.id}/role-connection
>
> Returns: applications role connection for the user.
>
> Scopes: `role_connections.write`

**Update User Application Role Connection**
> PUT /users/@me/applications/{application.id}/role-connection
>
> Returns: Updates and returns the application role connection
>
> Scopes: `role_connections.write`
>
> Params:
>
> |Field|Type|Description|
> |---|---|---|
> |platform_name?|string|the vanity of the platform a bot has connected (max 50 characters)|
> |platform_username?|string|the username on the platform a bot has connected (max 100 characters)|
> |metadata?|object|object mapping application role connection metadata keys to their `string` -ified value (max 100 characters) for the the user on the platform a bot has connected|
