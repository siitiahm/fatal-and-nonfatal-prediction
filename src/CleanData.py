import argparse
import sys

'''
function to clean data file. remove attributes that are irrelevant/numerical for now.
input_file = command line argument. name of txt file with unclean data 
                                   (outputted from splitdata in lab 3)
output_file = output will be named whatever the input name is, but 
              followed by -cleaned instead.
'''
def clean(input_file, output_file):
    formatteddata = [] # list to hold all formatted data.
                       # This array will be used to export
                       # newly cleaned data to output file.

    with open(input_file, encoding="UTF-8") as data:
        atts = data.readline().split(',') # first get the attribute names

        # filter noisy/irrelevant data
        keep = (1, 2, 3, 4, 5, 7, 9, 10, 11) # indices of the attributes i want to keep
        attstokeep = [] # to hold the names of the attributes i am using

        for att in atts:
            if atts.index(att) in keep: # if the attribute is one of the ones i want to keep
                attstokeep.append(att) # add it to a new list
        formatteddata.append(attstokeep) # this will be the first line of the file

        for line in data: # for the rest of the lines
            entry = [] # this will be used to hold the values of the atts we want to keep
            line = line.split(',')
            print(line)
            for attentry in line: # for each value in the line (separated by commas)
                if line.index(attentry) in keep: # if the value is for one of the attributes i want to keep
                    entry.append(attentry) # add to that list
            formatteddata.append(entry) # and then add that to our total data
    print(formatteddata)

# TODO: add a function or additional code to clean() to manipulate some data.
#   i.e. in att 'fatal' instead of 'n' for nonfatal and 'f' for fatal, should
#   be 0 or 1. Same for atts containing classes like m/f and maybe 0 for 'w'
#   (white) and 1 for all other classes (non-white i.e. 'b', 'u', etc.)

# TODO: add to clean() or write function to write cleaned and manipulated data
#   to output file.

'''
TO RUN - if running in IDE make sure file name is in your config settings in "parameters"
         if running just in command, make sure txt file is in same folder as CleanData.py
python (or py if in windows) CleanData.py training-uncleaned.txt

IF THAT DOESN'T WORK RUN
python (or py if in windows) -m CleanData.py training-uncleaned.txt
'''
def main():
    input = sys.argv[1]
    print(input)
    output_name = input[0:input.index("-")]
    output_name = output_name + "-clean.txt"
    clean(input, output_name)

if __name__ == "__main__":
    main()