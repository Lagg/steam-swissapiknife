#!/usr/bin/env python

import urllib.request, urllib.error, urllib.parse, json, sys
import argparse
from pprint import pprint

cmdline = argparse.ArgumentParser(description = "Carve up some API docs in list or wiki format")

cmdline.add_argument("key",
        help = "Your API key")

cmdline.add_argument("-f", "--format", choices = ["list", "wiki"], default = "list",
        help = "Print out API docs in condensed list form or wikitext")

cmdline.add_argument("-i", "--interface", default = None,
        help = "Only print methods in this interface")

cmdline.add_argument("-m", "--method", default = None,
        help = "Only print methods with this name")

opts = cmdline.parse_args()

key = opts.key
request_url = "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=" + key
url_root = "http://api.steampowered.com/"

apilist = json.loads(urllib.request.urlopen(request_url).read().decode("utf-8"))
api_names = []
api_methods = {}
mw_skeleton = (opts.format == "wiki")

for api in apilist["apilist"]["interfaces"]:
    api_names.append(api["name"])
    api_methods[api["name"]] = api["methods"]

api_names.sort()

for api in api_names:
    if opts.interface and api != opts.interface:
        continue

    methods = api_methods[api]
    for method in methods:
        param_doc_lines = []
        if opts.method and method["name"] != opts.method:
            continue

        querypart = ["key=" + key]
        for param in method["parameters"]:
            name = param["name"]
            ptype = param["type"]
            optional = param["optional"]
            desc = param.get("description", '')

            ptypewrapper = "<{1}>"
            if optional: ptypewrapper = "[{1}]"

            if name != "key":
                querypart.append(("{0}=" + ptypewrapper).format(name, ptype))

            if mw_skeleton:
                if optional: name = "{{API optional|" + name + "}}"
                param_doc_lines.append(";{0} ''({1})'': {2}".format(name, ptype, desc))
            else:
                param_doc_lines.append(name + ": " + desc)

        fullurl = url_root + api + '/' + method["name"] + '/v' + str(method["version"])
        if mw_skeleton:
            print("Page URL: " + "http://wiki.teamfortress.com/wiki/WebAPI/" + method["name"] + "\n")
            print("== URL ==\n<nowiki>{1} {0}</nowiki>\n\n== Method-specific parameters ==".format(fullurl, method["httpmethod"]))
        else:
            print(method["httpmethod"] + ' ' + fullurl + '?' + "&".join(querypart))

        print('\n'.join(param_doc_lines))

        if mw_skeleton:
            print("\n== Result data ==\n")
        print('\n')
