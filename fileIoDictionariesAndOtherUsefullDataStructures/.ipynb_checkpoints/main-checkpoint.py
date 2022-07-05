#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  main.py
#  Copyright 2018 Eric Eckert <dukeleto@spica>
"""
Lesson 3, file io and dictionary (hash) tables
Dictionaries are just like lists except without the IO hit
They are also very good for command and control
Show them how to manipulate all of this stuff in the shell as a debug technique
Nestability and interoperatbility
"""
import json
Fname = "rFile.ini"

def loadPF(Fname):
    pfContents = [] #a list
    with open(Fname,'r') as fileObject:
        #this is called a list comphrension
        pfContents = [line.strip() for line in fileObject if("#" not in line.strip())]
    #attempt to jsonify
    #r is to indicate that this is a raw string (i.e ignore \ escape charecter
    pfContents = json.loads(r''.join(pfContents))
    return pfContents

def loadPFLongForm(Fname):
    pfContents = [] # a list
    fileObject = open(Fname,'r')
    for line in fileObject:
        if("#" not in line.strip()):
            pfContents.append(line.strip())
    #attempt to jsonify
    #r is to indicate that this is a raw string (i.e ignore \ escape charecter
    pfContents = json.loads(r''.join(pfContents))
    #close the file
    fileObject.close()
    return pfContents
  
aListComprehension = [i for i in range(2,100,2)]
aDictionary = {}
aDictionary["Eric"] = [23,"California"]
aDictionary["Hannah"] = [19,"Nevada"]
print("Dictionary aDictionary has keys " + str(aDictionary.keys()))
#you can very easily iterate over lists
for i in range(len(aListComprehension)):
    print(aListComprehension[i])
#note that this is equivelent (but very slightly slower)
#the difference is that I am itterating over the contents of the list instead of the indexes of the list
for i in aListComprehension:
    print(i)
#you can iterate over dictionaries in much the same way as you can itterate over lists
for i in aDictionary.keys():
    print("Iterating of keys currently on key " + i)
    
