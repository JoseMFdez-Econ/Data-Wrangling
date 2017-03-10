# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

#DATADIR = "/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/"
DATADIR = ""
DATAFILE = "beatles-diskography.csv"
#datafile = os.path.join(DATADIR, DATAFILE)

def parse_file(datafile):
    data = []
    # 'rb' 'reads-binary': allows python to be more flexible in reading what's in the file.
    with open(datafile, "r") as f:

        # The method readlines() reads until EOF using readline() and returns a list
        # containing the lines.
        # Reads first line of file and split it using ","
        # This gives you a list of values you can use as 'keys items' for the
        # data items you pull on from the data file later on.
        header = f.readline().split(",") # By getting the 'headers' you use them as 'key'
                                         # and the lines split (by commas) as values
        #print header # These are the keys

        counter = 0
        for line in f: # Loop over the lines on the file 'f'
            if counter == 10: # Counter-> Makes sure considers up to the 10th line (not inclusive)
                break # Break if we have read 10 lines

            #print line # Execute-> you only see each line separated by commas

            # For every line up to the 10th line
            # We split the line again using the comma delimeter
            fields = line.split(',')
            #print fields # 'fields' are lists with the values
            entry = {} # Initialize an empty dictionary. The entry is going to be the data item
                       # that will construct using the 'keys' we got from the first
                       # line of the file ('header') and the indiviual line we processed obove (field)

            # Constructs the dictionary with the key-value pais.
            # By using 'enumerate' we get an 'index' value in addition to a value
            # for each item in the 'fields' list
            for i, value in enumerate(fields):
                #print i, value # i-> from 0-10 fields/variables (keys);
                                # value-> each corresponding value per line
                entry[header[i].strip()] = value.strip() # Assigns appropiate 'value' corresponding to each
                                            # field ('header') for that the i_th key for that particular field
            # Use 'strip()' to clean any empty space

            data.append(entry)
            counter += 1

    return data

#parse_file(DATAFILE)

## Test program


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    #print (datafile)
    d = parse_file(datafile)
    #print (d)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()

#print (parse_file(DATAFILE))
