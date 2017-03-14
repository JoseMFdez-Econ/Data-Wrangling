import os

#cpath = os.getcwd()
#print (cpath)
os.chdir("/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/coursera")
# handle = open(filename, mode)
# Doesn't read all the data in the file! It creates a connection between the
# memory and the data in the hard-drive.

# File has to be in the same folder as the python code is saved.
## The "New-Line Character" (e.g. Hello\nWorld!). "New-Line Character" is a character.

"""
xfile = open('mbox.txt')

for line in xfile: # reads every line in the file
    print line     # prints every line in the file

"""

"""
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1

print ('Line Count:', count)
"""

"""
## Read the Entire file - Do not use if the file is large!
fhand = open('mbox-short.txt')
inp = fhand.read()
print (len(inp))
print (inp[:20])
"""

"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Read the line and strip the '\n' from the end of the line
    if line.startswith('From:'):
        print (line)
"""

"""
## Skip 'uninteresting lines'
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Read the line and strip the '\n' from the end of the line
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting line'
    print (line)
"""

"""
## Using 'in' to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Read the line and strip the '\n' from the end of the line
    if not '@uct.ac.za' in line:
        continue
    print (line)
"""


## Prompt for file name
# fname = raw_input('Enter the file name: ') # Fot python 2.7
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ('File cannot be opened: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print ('There were', count, 'subject lines in', fname)
