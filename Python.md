# Python for Automation

## Agenda
- Motivation to learn Python
- Python applications in VLSI
- Python Overview
- Python Basics
- Command Line Arguments
- Varibales
- Lists
- Tuples
- Dictionary
- List of lists
- Operators, Loops
- Conditional statements
- Functions
- Working with text files
- Regular Expressions
- Exception Handling
- Regular Expressions - Practical Usage
- Data Structures using lists and tuples
- Pandas
- Object Oriented Programming
- Perl to Python porting
- Python Complex Examples
- Numpy

## Motivation to learn Python

Every job/domain has some kind of repetitive work, that engineer has to do manually

- Checking the run pass or fail status
 - Make report in different formats like xls, html, ppt, doc (word) etc.
- Creating environment files or removing some of the files
- Updating all existing files for some project specific updates
- Running testcases including compilation, elaboration and simulation
- Running same test with different configurations

Python reduces all the above effort by means of intelligent scripting, that reduces human manual effort and errors
Python scripts are reusable, the script can be implemented as a module, and that module can be used in other scripts

There is huge resource of Python packages (pre-implemented libraries) which makes it easy to do any kind of jobs across different work domains like VLSI, Embedded, Software

There are 1,00,000+ python packages
create xls, parse xls
create html, parse html, compare html

Python is open source, a Python package can be developed and released as part of Python packages
Python reduces manual effort and gives more time to focus on important aspects of job

## Python Overview

Python is Open Source, released as a basic set of Python Packages
User can install additional packages as needed.
pip install package_name
Else, downlaod, unzip and "Python setup.py install"

High level Interpreted programming language
High level means Python can treat entire line of cose as a single variable, while C language handles datatypes only at the character level

Compiled language (Ex: C, C++)
- Compilation and Linking
- Transformation to Machine code

Interpreted language (Ex: Python, TCL, perl)
- No Compilation
- Interpreter is required to execute the source code
 - Interpreter: /usr/bin/python3
- Python script is executed line by line without compilation
- If script has errors, it produces the output till it reaches error in the code, then exits at the line of error in code
- If there is no error in code, script will complete by executing till last line

Interactive language
- While script is being run, we can pass the inputs
Example
scanf in C language
Python also has similar concept

Object Oriented programming language
- Programming style that encapsulates code within objects

## Python Basics

### Python Version
Python has multiple releases, python 3.14.6 is the latest

To check Python version in Windows
cmd prompt
python --version

### Hello World Program
#!/usr/bin/python3
#Hello World Print Program
#to print the text to the screen
print ("Hello, World!!")
#to print without new line, the line will end with empty space
print ("Hello, World!!", end="")
#to print with new line
print ("Hello, World!!\n")

## Python Basics
Python programming in Interactive mode
To enter into Python prompt, type "python"
you will be able to see >>>
Mow enter your python commands
>>> print ("Hello, Python!")

\# is used to commnet in python
\\ used to indicate special characters
\\" used to indicate "

## Lines and Indentation
In Python,
- semicolon is not compulsory at end of the line
- block of code can be defined using indentation 
- no need to use the following to indicate block of code
 - begin
 - end
 - ","
 - { }

The number of spaces in the indentation is variable, but all statements within the block must be indented with the same number of spaces

The following code generates error
if True:
print ("Answer")
print ("True")
else:
print ("Answer")
print ("False")

#Correct Code
if True:
	print ("Answer")
	print ("True")
else:
	print ("Answer")
	print ("False")

## Python Identifiers
Name used to identify a variable, function, class, module or other objects

A python variable name starts with
- either a letter A to Z or a to z
- underscore followed by zero or more letter
- underscore followed by digits (0-9)

Python is case sensitive

In Python, Class names start with uppercase letter, while all other identifiers can start with lowercase letter
Starting an identifier with a one leading underscore "\_" indicates indentifier is private
Example in C++, varibale is declared as local, potected (private)
But in Python, just start with "\_" to the variable name
Example
\_varname
varname becomes a private identifier

Starting an identifier with two leading underscore "\_" indicates indentifier is strongly private
Example
\_\_varname
varname becomes a strongly private identifier

If the identifier also ends with two trailing underscore indicates identifier is language defined special variable name
Example
\_\_varname\_\_
varname becomes Python language defined special variable name

## Multi Line Statements

Statements in Python typically end with a new line
Continuation character "\\" used to denote that the line should continue
Example
total = item_one + \
	item_two + \
	item_three

Statements contained within the [], {} or () brackets do not need to use the line continuation character
days = ['Monday', Tuesday',
	'Wednesday', Thursday',
	'Friday']

## Quotation
Python accepts 
single (')
double (")
triple (''' or """) quotes to denote string literals.
As long as the same type of quote starts and ends the string

The triple quotes are used to span the string across multiple lines
word = 'word'
sentence = "This is a sentence"
paragraph = """This is a paragraph. It is
		made up of multiple lines
		and sentences"""
## Comments
A hash sign "\#" that is not inside a string literal begins a comment
All characters after the "\#" upto the end of the physical line are part of the commnent and Python interpreter ignores them

Tripe quoted string is also ignored by Python interpreter and can be used as a multiline comments

'''
This is
a  multiline
comment
'''






- Python Modules
 - import module_name
  - Example:
   - import os
   - import re
    - re.match, re.replace
- Built in methods and methods that come with modules






 





 
 
