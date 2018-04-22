#!/usr/bin/env python

import json


loaded_ble = json.load(open("ble.json","r"))
handles = list()

for item in loaded_ble:
    try:
        print item["_source"]["layers"]["btatt"]["btatt.handle"]
        print item["_source"]["layers"]["btatt"]["btatt.value"]
    except:pass

print handles