#!/usr/bin/python3
"""
This is script adds all arguments to a python list, and save them
in to a json file called add_item.json

Usage:
    ./7-add_item.py <arguments>
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


saveArgumentsFile = 'add_item.json'
loadedList = []

try:
    loadedList = load_from_json_file(saveArgumentsFile)
except FileNotFoundError:
    pass

argsList = sys.argv[1:]

addedList = loadedList + argsList

save_to_json_file(addedList, saveArgumentsFile)
