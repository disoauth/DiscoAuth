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
    :classmethod:

    Makes the actual url and returns it

    :return: The auth link
    :rtype: str
