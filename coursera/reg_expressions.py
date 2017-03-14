import os
import re # Regular Expressions library

#cpath = os.getcwd()
#print (cpath)
os.chdir("/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/coursera")


## Regular Expressions

"""
# Not using regular Expressions
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print (line)
"""
# Regular Expressions Notes:
# (1) re.search() returns True/Flase depending on whether
    # the string matches the regular Expression.
# (2) re.findall() is used if we want the matching string
    # to be extracted as a python list.


"""
# Using Regular Expressions
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line): # Only lines that have 'From:' in the begining
                                  # Same as-> if line.startswith('From:'):
        print (line)
"""

# Regular Expressions Notes:
# (1) '^' Starts with
# (2) '.' The 'dot' character matches any character
# (3) '*' If you add astertisk character, the character is " any number of times"
    # For example: (^X.*:) -> Match the start of the line, followed by the letter 'X'
    # followed by any character, as many times as possible, before ':'

    # For example: (^X-\S+:)-> (^) Match the start of the line, followed by 'X-',
    # (\S) match any non-white character, (+)one or more times, before ':'

"""
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print (y)
"""

# Regular Expressions Notes:
# (1) Syntax with '[]' encloses a set. Inside the '[]' is a single character and
    # it contains the legal 'things' we are willing to take.
    # Example: [0-9]+ -> '[0-9]'  A (one) digit, (+) one or more digits.
    # Asking Python: Find one or more digits (at least 1) and give it back to me.
"""
y = re.findall('[AEIOU]+', x) # Find all the sequences where there are 1 or more
                              # upper casae vowels
print (y)  # Returns an empty list
"""


## Note: These matching operations are greedy. That means that as they extract
## they push outwards and wants to return the largest possible string. For exmaple:

"""
x = 'From: Using the : character'
y = re.findall('^F.+:', x) # Extract a line (^) begining with an 'F', (.) any character,
                            # one or more times.
print (y) # >> ['From: Using the :'] -> 'Greedy' says: Prefer the lastgest string
          # Both strings match (i.e. 'From:' and 'From: Using the :'), but greedy
          # prefers 'From: Using the :'
## To stop the greedy-matching add '?'

y = re.findall('^F.+?:', x)
print (y) # >> ['From:']
"""


## Section 2 - More complicated
# You can use '()' to select exactly what we want to match (return)

"""
fhand = open('mbox-short.txt')
list = []
for line in fhand:
    line = line.rstrip() # Read the line and strip the '\n' from the end of the line
    # (^) Find a line that starts with 'From ', followed by a 'blank-space'; followed by
    # the thing inside the '()'[... start the match...]; (\S) look for non-blank characters;
    # (+) at least one (one or more); followed by an (@) sign; (\S+) followed by one or more
    # non-blank characters; (')') and stop match.
    y = re.findall('^From (\S+@\S+)', line) # Give me back on the things inside the '()'
    if len(y) != 0:
        print (y)
"""

"""

fhand = open('mbox-short.txt')
list = []
for line in fhand:
    line = line.rstrip()
    y = re.findall('@([^ ]*)', line) # Inside the '[]', '^' means not!
                                    # Find an '@' sign, start matching... and
                                    # match non-blank characters as many as possible '(*)'
                                    # up to you find a blank-character.
    if len(y) != 0:
        print (y)
"""

"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # (^) Find a line that starts with 'From ', followed by a 'blank-space'; followed by
    # (.*) any number of characters, until I find an '@' sign and ...start extracting...
    # and keep going until we don't find a blank-space and stop stracting when we find a
    # blank-space.
    y = re.findall('^From .*@([^ ]*)', line)
    if len(y) != 0:
        print (y)
"""

fhand = open('mbox-short.txt')
numlist = []
for line in fhand:
    line = line.rstrip()
    # Find a line that starts with 'X-DSPAM-Confidence:' and a blank-space;
    # then ...start-matching... a [0-9.] digit or period, one or more (at least one)
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :
        continue
    num = float(stuff[0])
    #print (num)
    numlist.append(num)

print ('Maximum: ', max(numlist))
