# *requests* module for Package Control
[![Build Status](https://travis-ci.org/packagecontrol/requests.png?branch=master)](https://travis-ci.org/packagecontrol/requests)


This is the *[requests][]* module
bundled for usage with [Package Control][],
a package manager
for the [Sublime Text][] text editor
and its Python 3.3 plugin host.
For the 3.8 host,
the .whl archives are directly fetched from pypi.


this repo | pypi
---- | ----
![latest tag](https://img.shields.io/github/tag/packagecontrol/requests.svg) | [![pypi](https://img.shields.io/pypi/v/requests.svg)][pypi]


## How to use *requests* as a dependency

In order to tell Package Control
that you are using the *requests* module
in your ST package,
create a `dependencies.json` file
in your package root
with the following contents:

```js
// For Python 3.3
{
   "$schema": "sublime://packagecontrol.io/schemas/dependencies",

   "*": {
      "*": [
         "requests"
      ]
   }
}
// For Python 3.8 & ST4
{
    "$schema": "sublime://packagecontrol.io/schemas/dependencies",

    "*": {
        "*": [
            "requests",
            "charset-normalizer",
            "idna",
            "urllib3"
        ]
    }
}
```

If the file exists already,
add `"requests"` to the every dependency list.

Then run the **Package Control: Satisfy Dependencies** command
to make Package Control
install the module for you locally
(if you don't have it already).

After all this
you can use `import requests`
in any of your Python plugins.

See also:
[Documentation on Dependencies](https://packagecontrol.io/docs/dependencies)


## How to update this repository (for contributors)

Don't. 
We're already mirroring the latest 3.3-compatible version
and for the 3.8 host,
the package is directly fetched from pypi.


## License

The contents of the root folder
in this repository
are released
under the *public domain*.
The contents of the `all/` folder
fall under *their own bundled licenses*.


[requests]: http://docs.python-requests.org/en/latest/
[Package Control]: http://packagecontrol.io/
[Sublime Text]: http://sublimetext.com/
[pypi]: https://pypi.python.org/pypi/requests
