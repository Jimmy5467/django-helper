import os
import sys
import fileinput

print("Text to search for:")
textToSearch = input("> ")

print("Text to replace it with:")
textToReplace = input("> ")

print("File to perform Search-Replace on:")
fileToSearch = input("> ")
# fileToSearch = 'D:\dummy1.txt'
# Read in the file
with open(fileToSearch, 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace(textToSearch, textToReplace)

# Write the file out again
with open(fileToSearch, 'w') as file:
    file.write(filedata)

input('\n\n Press Enter to exit...')
