# Discord Api

## User

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

### User Links
**Get Current User**
> GET /users/@me
>
> Headers: Access Token
> 
> Scopes: Identify (email if you want the response to include the user's email)

**Get User**
> GET /users/{user.id}
>
> Headers: Access Token
>
> Scopes: Identify (email if you want the response to include the user's email)
> 
> returns a user object for a given user ID
