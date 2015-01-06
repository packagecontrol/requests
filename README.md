# requests
[![Build Status](https://travis-ci.org/packagecontrol/requests.png?branch=master)](https://travis-ci.org/packagecontrol/requests)


This is the [requests][] package
bundled for usage with [Package Control][],
a package manager
for the [Sublime Text][] text editor.


this repo | pypi 
---- | ----
![latest tag](https://img.shields.io/github/tag/packagecontrol/requests.svg) | [![pypi](https://pypip.in/version/requests/badge.svg)][pypi]


## How to use `requests` as a dependency

In order to tell Package Control
that you are using the `requests` package
in your ST package,
create a `dependencies.json` file
in your package root
with the following contents:

```js
{
   "*": {
      "*": [
         "requests"
      ]
   }
}
```

If the file exists already,
add `"requests"` to the every dependency list.

Then run the **Package Control: Satisfy Dependencies** command
to make Package Control
install the package for you locally
if you don't have it already
(or restart ST).

See also:
[documentation on dependencies](https://packagecontrol.io/docs/dependencies)


## How to update this repository (for contributors)

1. Download the latest tarball
   from [pypi][].
2. Delete everything inside the `all/` folder.
3. Copy the `requests` folder,
   `test_requests.py`,
   `requirements.txt`
   and everything related to copyright/licensing
   from the tarball
   to the `all/` folder.
4. Commit changes
   and either create a pull request
   or create a tag directly
   with the format `v<version>`.

   Finally, don't forget to push.

The reason why `loader.py` exists
is because Package Control 3.0.0
does not yet allow the same code base
for both ST2 and ST3.


## License

The contents of the root folder
in this repository
are released
under the *public domain*.
The contents of the `all/` folder
fall under *their own bundled licenses*.


[requests]: https://github.com/kennethreitz/requests
[Package Control]: http://packagecontrol.io/
[Sublime Text]: http://sublimetext.com/
[pypi]: https://pypi.python.org/pypi/requests
