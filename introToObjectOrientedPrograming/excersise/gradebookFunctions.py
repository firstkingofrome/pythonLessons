#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gradebookFunctions.py
#  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import json

"""
addAssignment:add an assignment to the grade book
gradeBook:dict:dictionary contianing the grade book for this class
studentName:str:the students name
assignmentName:str:the name of the assignment to be added
assignmentGrade:float:the grade
return:dict:the updated grade book
"""

def addAssignment(gradeBook,studentName,assignmentName,assignmentGrade):
    gradeBook[studentName]["assignments"][assignmentName]=assignmentGrade
    return gradeBook




"""
saveGradeBook:saves the curent grade book dictionary as a nicely formatted json file
gradeBookName:str: Name of the json file to be written
gradeBook:dict:Dictionary containing the grade book
"""

def saveGradeBook(gradeBookName,gradeBook):
    """
    When I was writing this realized that I have not explained "with"
    the commented with code is equivelent to the following:
    it simply closes the file handle for you automatically 
    its easy to remember since it is grammaticaly a lot like saying:
    with file open as fileHandle:
        doStuff()
    """
    fileHandle=open(gradeBookName, 'w')
    json.dump(gradeBook,fileHandle, indent=4, sort_keys=True)
    fileHandle.close()
    """
    with open(gradeBookName, 'w') as fileHandle:
        #save the dictionary to a file and make the output "pretty"
        json.dump(gradeBook,fileHandle, indent=4, sort_keys=True)
        #json.dump(gradeBook, fileHandle)
    """ 
    
def loadGradeBook(fname):
    try:
        with open(fname, 'r') as fileHandle:
            data = json.load(fileHandle)
        return data
    except FileNotFoundError:
        print("The file \'" + str(fname) + "\' doesnt appear to exist")
        return None





