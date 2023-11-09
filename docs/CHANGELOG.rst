=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[`Unreleased`_]
===============

Added
-----

- `#53 <https://github.com/disoauth/DiscoAuth/pull/53>`_ CLI Update (The big point of the next version)

[`1.1.2`_] - October 25, 2023
=============================

Added
-------

* Added the :class:`UserObj` to the documentation


[`1.1.1`_] - October 25, 2023
=============================

Changed
-------

* The goals in the README from the v1.0.0 goals to v2.0.0 goals

[`1.1.0`_] - October 25, 2023
=============================

Added
-----

* Documentation, using `Read The Docs <https://readthedocs.io>`_ and `Sphinx <https://www.sphinx-doc.org/en/master/usage/index.html>`_
* `#18 <https://github.com/disoauth/DiscoAuth/pull/18>`_ A model for user data

[`1.0.1`_] - September 22, 2023
===============================

Nothing important happened for this update

[`1.0.0`_] - September 22, 2023
===============================

Added
-----

* `#7 <https://github.com/disoauth/DiscoAuth/pull/7>`_ The subclass, :class:`User` to :class:`discordApi`
* A method in the new :class:`User` class to get user data
* A method to make the auth url in the AuthUrl class

Fixed
-----

* The state generation

[`0.2.1`_] - September 18, 2023
===============================

Changed
-------

* Renamed Package from :code:`DisOAuth` to :code:`Async-DisOAuth` to accomodate for the Sync version of :code:`DisOAuth`

  * (Later, the Sync version would be discontinued)

[`0.2.0`_] - September 15, 2023
===================================================================================

Added
-----

* The :class:`discordApi` class
* The :meth:`discordApi.accessToken` method, to get the access token of a user
* A method of :class:`discordApi` to check the app's auth info
* MIT License

[`0.1.4`_] - September 13, 2023
===================================================================================

Changed
-------

* Package renamed from :code:`DiscordOAuth2` to :code:`DisOAuth`

[`0.1.3`_] - September 13, 2023
===================================================================================

Changed
-------

* Package renamed from :code:`DiscordOAuth-Helper` to :code:`DiscordOAuth2` 

[`0.1.2`_] - September 13, 2023
===================================================================================

Added
-----

* The authors in pyproject.toml [`Commit <https://github.com/disoauth/DiscoAuth/commit/dd673466ba882fa6dca4bd1dbfa793158878b2d3>`_]

[`0.1.1`_] - September 13, 2023
===================================================================================

Changed
-------

* publish.yml (The workflow to publish the package) was moved to DiscordOAuth2(the earlier name of the repo)/.gituhb/workflows from the root directory

[`0.1.0`_] - September 13, 2023
=================================================================================

Added
-----

* The AuthUrl class, that would return the auth url
  * Added a function to make the state for the auth url


.. _Unreleased: https://github.com/disoauth/DiscoAuth/compare/v1.3.0...cli
.. _1.3.0: https://github.com/disoauth/DiscoAuth/compare/v1.2.0...v1.3.0
.. _v1.2.0: https://github.com/disoauth/DiscoAuth/compare/v1.1.5...v1.2.0
.. _1.1.2: https://github.com/disoauth/DiscoAuth/compare/v1.1.1...v1.1.2
.. _1.1.1: https://github.com/disoauth/DiscoAuth/compare/v1.1.0...v1.1.1
.. _1.1.0: https://github.com/disoauth/DiscoAuth/compare/v1.0.1...v1.1.0
.. _1.0.1: https://github.com/disoauth/DiscoAuth/compare/v1.0.0...v1.0.1
.. _1.0.0: https://github.com/disoauth/DiscoAuth/compare/v0.2.1...v1.0.0
.. _0.2.1: https://github.com/disoauth/DiscoAuth/compare/v0.2.0...v0.2.1
.. _0.2.0: https://github.com/disoauth/DiscoAuth/compare/v0.1.4...v0.2.0
.. _0.1.4: https://github.com/disoauth/DiscoAuth/compare/v0.1.3...v0.1.4
.. _0.1.3: https://github.com/disoauth/DiscoAuth/compare/v0.1.2...v0.1.3
.. _0.1.2: https://github.com/disoauth/DiscoAuth/compare/v0.1.1...v0.1.2
.. _0.1.1: https://github.com/disoauth/DiscoAuth/compare/v0.1...v0.1.1
.. _0.1.0: https://github.com/disoauth/DiscoAuth/tree/v0.1
