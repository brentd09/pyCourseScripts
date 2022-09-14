#!/usr/bin/env python
"""Usage - this is how the script works"""
import sys,inspect,os
#PS $PSVersionTable - gives the PS version
print(sys.version_info)

#PS Not case sensitive for most things
'Name' == 'name' #PY these strings are not the same, python is case sensitive for everything
'name' == 'name' #PY this will show true

#PS Indenting is just a great idea it is not mandatory
items = ['this','is','a','list','of','items']
for item in items:
  print(item)      # this line indented means that it is part of the for loop
print('THE END')   # this line that is not indented is not part of the loop

#PS # means single line comment. <# this is a block comment that can span multiple lines  #>
# This is a single line comment
''' 
  this is a block
  comment that can
  span many lines
'''

#PS Variables: when using them on the command line add $ to the name: $VarName
varname = "this is the contents of the variable"
#PS to display the contents of a variable in PS $VarName
print(varname)

#PS write out to screen Write-Host "This is the message that will appear"
print("This is the message that will appear")

#PS input from keyboard $Response = Read-Host -Prompt 'Please enter something'
response = input('Please enter something: ')

#PS parameter input: Param([string]$ComputerName)
import sys
print(sys.argv)     # this will use the sys module to discover everything from the command line [0] is the command [1] is the first arg/parameter
if len(sys.argv) > 1:
  print(sys.argv[1])  # Shows the first parameter value after the command name which is [0]

#PS object members: 'This is a string' | Get-Member
import inspect
string1 = 'This is a string'
members = inspect.getmembers(string1)   # This produces a list of object members
for member in members:
  print(member)

# PS collectons: @() array, @{} hashtable, @' '@ or @" "@ here strings
#  List: is a collection which is ordered and changeable. Allows duplicate members.
#  Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
#  Set: is a collection which is unordered and unindexed. No duplicate members.
#  Dictionary: is a collection which is ordered* and changeable. No duplicate members.
listobj = [1,2,3,4]  # Mutable
tupleobj = (1,2,3,4)  # Immutable
setobj = {1,2,3,4} # Mutable
dictionaryobj = {'key1':1,'key2':2,'key3':3,'key4':4} # Mutable - this is also called a hashtable

#PS Object[]:  $ObjArray = @(1,2,3,4)
objarray = (1,2,3,4)

#PS ArrayList: [System.Collections.ArrayList]$AL = @(1,2,3,4)
al = [1,2,3,4]

#PS HashTables $HT = @{Name='bob';Age=21;DOB='1960-8-21'}
import inspect
ht = {'givenname':'Bob','Age':21,'DOB':'1960-8-21'}
#PS Add to HashTables $HT.Add('Surname','Builder')
ht['surname']='Builder'

#PS Type of Object: 'This is a string'.GetType().FullName
type('This is a string')

#PS TypeCasting: [String]$Number [int]$Val or $Val -as [int]
int('123')
# int('string')  # this will fail of course
str(123)
chr(90)
bool(0) # 0 - False, nonzero - True
hex(1234)
bin(1234)

# PS Where: ("The ducks fly backward in fall") -split ' ' | Where-Object {$_ -notlike 'f*'}
import re
patn = re.compile("^[^f]")  # using REGEX is the best way to check for matches in python
items = filter(lambda x: re.match(patn, x),"The ducks fly backward in fall".split(' ') )
for item in items:
  print(item)


