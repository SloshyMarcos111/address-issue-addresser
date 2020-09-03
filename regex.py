# -*- coding: utf-8 -*-
import re

f = open("addresses.csv")

for address in f:
    print address
    match = re.split('(\d.+)', address)

for string in match:
    print string

