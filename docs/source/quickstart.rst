Quickstart
=====

Before we can get the oauth url, we need to install and setup DisOAuth

.. _installation:

Installation
------------

To use DisOAuth, you need to first install it using pip:

.. code-block:: console

  (.venv) $ pip install Async-DisOAuth


Now it's time to make the url

.. _auth-url:

Authorization URL
-----------------

To make a url, you'll need to use the :func:`makeUrl` function from the :class:`AuthUrl` class:

.. py:class:: AuthUrl(client_id, scope, redirect_uri)

  Stores the client id, the scopes you want, and the redirect_uri

  :param client_id: Your app's client id
  :param scope: The scope of your app
  :param redirect_uri: The redirect uri of your app
  :type client_id: str
  :type scope: List[str]
  :type redirect_uri: str
  :return: Nothing, it's a class
  :rtype: NoneType

  .. py:function:: makeUrl()

  :return: The auth url.
  :rtype: str



