import os
import pprint
import csv # https://docs.python.org/2/library/csv.html

#DATADIR = ""
DATADIR = "/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    # 'rb' 'reads-binary': allows python to be more flexible in reading what's in the file.
    with open(datafile, "r") as sd:
        r = csv.DictReader(sd) # Assumes we want to read all our data into dictionaries
                                # Assumes first row contains headers and those names we
                                # want to use as "fields"
                                # Creates a dictionary for each row and keys will be the fields
                                # from the headers and values would be the rows associated with them.

        for line in r: # Loop through the dictionaries 'r'
            print (line)
            #data.append(line)
    return data

parse_file(DATAFILE)
