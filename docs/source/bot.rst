Bot
===

.. toctree::

  
.. important::
  This guide assumes you have checked out the :doc:`quickstart` guide

In v1.3 the :class:`bot` was added, along with :class:`permissions` class and the ``permissions`` argument to the :class:`AuthUrl`, allowing for bot auth url's to be made and used to invite a bot to a guild.

Now the first thing we need to do is add the `bot` and `permissions` classes, and save the client id to a variable

.. code-block:: python
  :lineno-start: 1
  :caption: bot.py
  
  from DisOAuth import bot, permissions

  clientID = {Your bot's client id}

Now we can set up the permissions
  
Permissions
-----------

Depending on what you want your bot to do, you will need to use certain permissions, to learn what each permission does (and if there is a permission group you can use) check out the :doc:`api: documentation and the :doc:`permissions` documentation

To make this easier to understand, I will be using the Advanced permission group, or just administrator

.. code-block:: python
  :lineno-start: 5
  :caption: bot.py
  
  perms = permissions("administrator")

Now we have some basic permissions

.. warning::
  Using administrator as your permissions during testing is ok, but you should definitely specify only the permissions you need for your bot to work

  This is because if your bot gets hacked, you don't want the servers of the people who use your bot to get nuked or scammed.

Time to set up the bot url!

Bot Auth
--------

To make the bot



