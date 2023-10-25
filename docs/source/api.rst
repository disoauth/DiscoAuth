API
===

.. py:class:: AuthUrl(client_id, scope, redirect_uri)

  the base of the authorization url

  :param client_id: The client id of your app
  :param scope: A list of Discord scopes
  :param redirect_uri: The redirect uri you want to use
  :type client_id: str
  :type scope: List[str]
  :type redirect_uri: str

  .. py:method:: makeUrl()
    :async:

    Makes the actual url and returns it

    :return: The auth link
    :rtype: str

.. py:class:: discordApi(client_id, client_secret, scope, redirect_uri)

  Where you can get your access token, and use some Discord API links

  :param client_id: The client id of your app
  :param client_secret: The client secret of your app
  :param scope: a list of the scopes you authorized for
  :param redirect_uri: The redirect_uri you want to use
  :type client_id: str
  :type client_secret: str
  :type scope: List[str]
  :type redirect_uri: str

  .. py:method:: accessToken(code)
    :async:

    Makes a request to discord to get an access token

    :param code: The code that you get after the user gets redirected to your application
    :type code: str
    :return: The response recieved after the request is made
    :rtype: dict[str, str]

  .. py:class:: User(access_token)

    The links for the User API in Discord

    :param access_token: The access token you get after using the :meth:`accessToken` method in the :class:`discordApi` class

    .. py:method:: get_current_user()
      :async:

      Uses the access token provided to request the current user from discord api

      :return: The response from the Discord API
      :rtype: :class:`UserObj`

    .. py:method:: get_user_guilds()
      :async:

      Gets the users guilds from Discord

      :return: A list of partial Guild objects
      :rtype: List[str]

      .. versionadded:: 1.1
        Used to get the users guilds.

Models
------

.. important:: 

  None of the classes, functions, methods, or objects mentioned below are meant to be set by the user, only by the package

The models are what I use to return a object that is sent from Discord Api

.. py:class:: UserObj(payload)
    
  .. py:property:: id

    The user's id

  .. property:: username

    The user's username (not always unique)

    :type: str
    
  .. property:: discriminator

    the user's Discord-Tag

    :type: str

  .. property:: global_name

    The display name. For bots, it's the application name

    :type: str | None
    
  .. property:: avatar

    The user's avatar hash

    :type: str | None
    
  .. property:: bot

    Whether the user is a bot or not

    :type: bool
    
  .. property:: system

    Whether the user is a part of the Discord System or not

    :type: bool
    
  .. property:: mfa_enabled

    Whether the user has Multi-Factor Authentication on or not

    :type: bool
    
  .. property:: banner

    The user's banner hash.

    :type: str | None
    
  .. property:: accent_color

    The user's banner color, as a hexadecimal

    :type: int | None
    
  .. property:: locale

    The user's selected language option

    :type: str
    
  .. property:: verified

    Whether the user's email is verified or not

    :type: bool
    
  .. property:: email

    The user's email

    :type: str | None
    
  .. property:: flags

    The flags on the user's account

    :type: int | None
    
  .. property:: premium_type

    The type of nitro the user has

    :type: int | None
    
  .. property:: public_flags

    The public flags on a user's account

    :type: int | None
    
  .. property:: avatar_decoration

    The user's avatar decoration hash

    :type: str | None
    
  

    
    
