oslo.commonlibs
===============

A repository containing common code for the creation of an api service.

Usage
-----

Insert the following into the ```requirements.txt``` file of the API Service whose dependency you want the oslo.commonlibs to be.
```
oslo.commonlibs @ git+ssh://git@github.com/mkissam/oslo.commonlibs.git
```

```tox -e venv``` and ```tox``` will prompt you to enter your ssh password several times if the venv isn't yet created or activated.