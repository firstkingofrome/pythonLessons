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


