#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open("addresses.csv")
fixed = []

for address in f:
    match = re.split('(\d.+)', address)
    fixed.append(match)

for list in fixed:
    for string in list:
        print (string)

