#!/usr/bin/env python
"""steam-swissapiknife test suite"""

from steamswissapiknife import main
import unittest
import os
from contextlib import contextmanager
from io import StringIO
import sys

key = os.environ['STEAM_API_KEY']

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    
def test_interface_wiki_output():
    parser = main.parse_args(['-f', 'wiki', '-i', 'ITFItems_440', key])
    expected = """Page URL: http://wiki.teamfortress.com/wiki/WebAPI/GetGoldenWrenches

== URL ==
<nowiki>GET http://api.steampowered.com/ITFItems_440/GetGoldenWrenches/v2</nowiki>

== Method-specific parameters ==


== Result data =="""
    with captured_output() as (out, err):
        main.main(parser)
    output = out.getvalue().strip()
    assert(output == expected)
    
def test_interface_list_output():
    parser = main.parse_args(['-f', 'list', '-i', 'ITFItems_440', key])
    expected = """GET http://api.steampowered.com/ITFItems_440/GetGoldenWrenches/v2?key=%s""" % (key)
    with captured_output() as (out, err):
        main.main(parser)
    output = out.getvalue().strip()
    assert(output == expected)
    
def test_method_wiki_output():
    parser = main.parse_args(['-f', 'wiki', '-m', 'GetGoldenWrenches', key])
    expected = """Page URL: http://wiki.teamfortress.com/wiki/WebAPI/GetGoldenWrenches

== URL ==
<nowiki>GET http://api.steampowered.com/ITFItems_440/GetGoldenWrenches/v2</nowiki>

== Method-specific parameters ==


== Result data =="""
    with captured_output() as (out, err):
        main.main(parser)
    output = out.getvalue().strip()
    assert(output == expected)
    
def test_method_list_output():
    parser = main.parse_args(['-m', 'GetGoldenWrenches', key])
    expected = """GET http://api.steampowered.com/ITFItems_440/GetGoldenWrenches/v2?key=%s""" % (key)
    with captured_output() as (out, err):
        main.main(parser)
    output = out.getvalue().strip()
    assert(output == expected)