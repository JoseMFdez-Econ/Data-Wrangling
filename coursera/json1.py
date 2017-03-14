import os
import re # Regular Expressions library
import json # import JSON

#cpath = os.getcwd()
#print (cpath)
os.chdir("/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/coursera")

                #### 1 ####

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#info = json.loads(data)
#print ('Name:',info["name"])
#print ('Hide:',info["email"]["hide"])
#print ('Hide:',info["phone"]["number"])

                #### 2 ####

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input)
#print (info) # Prints a list
#print ('User count:', len(info))

for item in info:
    #print (item) # Prints 2 Dict, one for each 'id'
    print ('Name', item['name'])
    print ('Id', item['id'])
    print ('Attribute', item['x'])
