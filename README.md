## The Steam Swiss API Knife

A tool to explore the Steam API. The goal is to provide a simple
way for exploration and documentation of the API requests. Feel
free to contribute docs at http://wiki.teamfortress.com/wiki/WebAPI

### Using for API documentation

There is a feature in the swiss API knife intended to assist in
creating documentation pages on the [TF wiki](http://wiki.teamfortress.com/wiki/WebAPI).

To generate a skeleton page for the wiki API docs simply pass `-f wiki` when running the tool.
Also see the output of `-h` for more options for filtering. Refer to the existing API pages
for examples on the structure to use for the JSON output documentation.

### Installation
Run `python setup.py install`

### Tests

[![Build Status](https://travis-ci.org/Lagg/steam-swissapiknife.png)](https://travis-ci.org/Lagg/steam-swissapiknife)

Tests are run using `nose`.

Set the environment variable `STEAM_API_KEY` to your Steam API key before running tests.

Run `python setup.py test` after installation.
