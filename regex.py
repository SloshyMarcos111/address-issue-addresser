#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

"""
function that takes the blocks list and decomposes to the numbers in it
@:param blocks is a list of the second part of the addresses
"""
def get_numbers(blocks):

    address_num = []    # list of numbers in the address block

    # iterate through the blocks and append the numbers to the address_num list
    for block in blocks:
        numbers = re.findall(r'\d+', block)
        address_num.append(numbers)

    # print the numbers
    for number in address_num:
        print(number)


"""
function that takes in two section of the split address and prints each section with headings
@:param areas is a list of the first section of the address
@:param blocks is a list of the second section of the address
"""
def print_function(areas, blocks):
    print("------------------------- area section ---------------------------")

    for element in areas:
        print element

    print("------------------------- block section ---------------------------")

    for element in blocks:
        print element


# opening file that contains addresses with read only access
f = open("addresses.csv", "r")
fixed = []      # list of split addresses
areas = []      # first section of addresses (areas)
blocks = []     # second section of addresses (blocks)

# parsing file
for line in f:
    match = re.split('(\d.+)', line)    # splits entry in address file by the first digit encountered
    fixed.append(match)                 # appends the decomposed address into the split addresses list

f.close()   # close file

# appends the areas and blocks sections into respective lists
for subs in fixed:
    areas.append(subs[0])
    blocks.append(subs[1])

print_function(areas, blocks)   # call for printing the lists
get_numbers(blocks)             # get the numbers in the block list


