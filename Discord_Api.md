# Discord Api

## Base Links
> Base Api: 'https://discord.com/api'
>
> Authorization(header): 'Authroization: Bearer {access token}'
>
> Image Base Url: 'https://cdn.discordapp.com/'

## CDN
<details>
  
<summary>Contains some of the CDN links</summary>

Contains some of the CDN links, just make sure to add the image base url to the beginning

> Guild Icon
>
> icons/{{ guild.id }}/{{ guild.icon }}.png

> User Avatar
>
> avatars/{{ user.id }}/{{ user.avatar }}.png

</details>

## User
<details>
  
<summary>The user class, basically</summary>


  
### User Objects
<details>

<summary>All of the objects in the discord api user reference</summary>


## User Object
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
</details>

### User Links

<details>
<summary>All of the user links in the User links in the reference for the discord api</summary>

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
</details>
</details>

## Guild
<details>
<summary>The Guild class</summary>
  
### Guild Objects
<details>

|Field|Type|Description|
|---|---|---|
|id|snowflake|guild id|
|name|string|guild name (2-100 characters excluding trailing and leading whitspace)
|icon|?string|icon hash|
|icon_hash?|?string|icon hash, when returned in the template object|
|splash|?string|splash hash|
|discovery_splash|?string|discovery splash hash; only present for guilds with the "DISCOVERABLE" feature|
|owner?*|boolean|
|owner_id|snowflake|
|permissions?*|string|
|region? **|?string|
|afk_channel_id|?snowflake|
|afk_timeout|integer|
|widget_enabled?|boolean|
|widget_channel_id?|?snowflake|
|verification_level|integer|
|default_message_notifications|integer|
|explicit_content_filter|integer|
|roles|array of role objects|
|emojis|array of emoji objects|
|features|array of guild feature strings|
|mfa_level|integer|
|application_id|?snowflake|
|system_channel_id|?snowflake|
|system_channel_flags|integer|
|rules_channel_id|?snowflake|
|max_presences?|?integer|
|max_members?|integer|
|vanity_url_code|?string|
|description|?string|
|banner|?string|
|premium_tier|integer|
|premium_subscription_count?|integer|
|preferred_locale|string|
|public_updates_channel_id|?snowflake|
|max_video_channel_users?|integer|
|max_stage_video_channel_users?|integer|
|approximate_member_count?|integer|
|approximate_presence_count?|integer|
|welcome_screen?|welcome screen object|
|nsfw_level|integer|
|stickers?|array of sticker objects|
|premium_progress_bar_enabled|boolean|
|safety_alerts_channel_id|?snowflake|

\* These fields are only sent when using the `GET Current User Guilds` endpoint and are relative to the requested user

\** This field is deprecated and is replaced by `channel.rtc_region`
</details>

<details>

### Role Object

|Field|Type|Description|
|---|---|---|


</details>
