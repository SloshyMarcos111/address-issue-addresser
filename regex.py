# -*- coding: utf-8 -*-
import re

f = open("addresses.csv")
fixed = []

for address in f:
    #print address
    match = re.split('(\d.+)', address)
    fixed.append(match)

for string in fixed:
    print (string)

