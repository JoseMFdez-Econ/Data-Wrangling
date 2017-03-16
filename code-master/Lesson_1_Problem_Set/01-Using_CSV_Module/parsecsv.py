#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os
from collections import defaultdict

#cpath = os.getcwd()
#print (cpath)
os.chdir("/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/code-master/Lesson_1_Problem_Set/01-Using_CSV_Module/")

DATADIR = "/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/code-master/Lesson_1_Problem_Set/01-Using_CSV_Module/"
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'r', newline='') as f:
        header = f.readline().split(",")
        name = header[1].replace('"','')
        #name = name.replace('"','')
        has_header = csv.Sniffer().has_header(f.read(1024))
        #print (has_header)
        #print (f.seek(0))  # rewind
        reader = csv.reader(f) # Each row read from the csv file is returned as a list of strings.
        if has_header:
            next(reader)  # skip header row
        for row in reader:
            data.append(row)
        #pass
    # Do not change the line below
    #print (data)
    return (name, data)

#name, data = (parse_file(DATAFILE))

#print (name, data[0][1])


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
