Renaming
========

Soon, DisOAuth will be renamed to discoauth, and multiple methods will be renamed to follow the newly setup contributing guidelines. 
The functions will be duplicated, keep the original function, while renaming the others, and then the originals will be removed by v3.0

DisOAuth will recieve the v2.0 update, and bug fixes, if required.

DisOAuth will still be held by me, and you will still be able to get the previous versions

Also, the following functions will be depreciated and renamed:

* :class:`AuthUrl` ---> :code:`auth`
* :class:`AuthUrl` . :meth:`makeUrl` ---> :code:`auth.url()`
* :class:`discordApi` ---> :code:`discord`
* :class:`discordApi` . :meth:`discordApi.accessToken` ---> :code:`discord.token()`
* :class:`discordApi` . :class:`discordApi.User` ---> :code:`discord.user`
* :class:`discordApi` . :class:`discordApi.User` . :meth:`discordApi.User.get_current_user` ---> :code:`discord.user.fetch()`
* :class:`discordApi` . :class:`discordApi.User` . :meth:`discordApi.User.get_user_guilds` ---> :code:`discord.user.guilds()`
* :class:`discordApi` . :class:`discordApi.User` . :meth:`discordApi.User.get_guild` ---> :code:`discord.guild.fetch()`

A new class, ``guild`` will be created for the guild fetch

The depreciated classes, and methods will still be available until **v3.0**


