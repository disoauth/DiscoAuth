Permissions
===========

The permissions can be setup using:

- the names of the permissions, or
- numbers based off of the value in the discord documentation for permissions

The permissions is imported using the :class:`permissions` class

.. code-block:: python
  :lineos:
  :caption: perms.py

  from DisOAuth import permissions

Permissions
-----------

+---------------------+------+
|Permissions (name)   |Number|
+=====================+======+
|create_instant_invite|0     |
+---------------------+------+
|kick_members         |1     |
+---------------------+------+
|ban_members          |2     |
+---------------------+------+
|administrator        |3     |
+---------------------+------+

