#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


"""
function that takes an element from the list of areas and appends the corresponding numbers in the correct format
@:param first an element from the list of areas from the decomposed addresses
@:param is a list of numbers element from the block numbers list of the addresses
@:return the combined address with the correct formatting
"""
# this is where the addresses will be reformatted
def combine(first, numbers_list):
    combined = first + numbers_list[0] + "-" + numbers_list[1] + "-" + numbers_list[2]
    return combined


"""
function that takes the blocks list and decomposes to the numbers in it
@:param blocks is a list of the second part of the addresses
"""
def get_numbers(blocks_list):
    address_num = []  # list of numbers in the address block

    # iterate through the blocks and append the numbers to the address_num list
    for block in blocks_list:
        numbers_in_blocks = re.findall(r'\d+', block)
        address_num.append(numbers_in_blocks)

    # print the numbers
    print("\n\n------------------------- block numbers ---------------------------")

    for number in address_num:
        print(number)

    return address_num


"""
function that takes in two section of the split address and prints each section with headings
@:param areas is a list of the first section of the address
@:param blocks is a list of the second section of the address
"""


def print_function(area_list, block_list):
    print("\n\n------------------------- area section ---------------------------")

    for element in area_list:
        print element

    print("\n\n------------------------- block section ---------------------------")

    for element in block_list:
        print element


# opening file that contains addresses with read only access
f = open("addresses.csv", "r")
fixed = []  # list of split addresses
areas = []  # first section of addresses (areas)
blocks = []  # second section of addresses (blocks)

# parsing file
print("\n\n------------------------- original addresses ---------------------------")
for line in f:
    print(line)
    match = re.split('(\d.+)', line)  # splits entry in address file by the first digit encountered
    fixed.append(match)  # appends the decomposed address into the split addresses list

f.close()  # close file

# appends the areas and blocks sections into respective lists
for subs in fixed:
    areas.append(subs[0])
    blocks.append(subs[1])

print_function(areas, blocks)  # call for printing the lists
numbers = get_numbers(blocks)  # get the numbers in the block list

combined_addresses = []
for i in range(len(areas)):
    combined_addresses.append(combine(areas[i], numbers[i]))

print("\n\n------------------------- reformatted address ---------------------------")
for element in combined_addresses:
    print(element)

