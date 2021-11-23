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
        formatteddata.append(atts) # this will be the first line of the file

        for line in data: # for the rest of the lines
            entry = [] # this will be used to hold the values of each entry/line
            line = line.split(',')

            for attentry in line: # for each value in the line (separated by commas)
                if len(line) == 9: # if the value is for one of the attributes i want to keep
                    entry.append(attentry.strip()) # add to that list
            formatteddata.append(entry) # and then add that to our total data

    formatteddata = convertValToBinary(formatteddata) # call function to convert all values to numerical
    formatteddata = stringsToInt(formatteddata) # call function to manipulate data w/ multiple answers for one att

    # write to file
    with open(output_file, "w") as out_file:
        for line in formatteddata:
            for val in line:
                out_file.write(str(val))
                out_file.write(" ")
            out_file.write("\n")

'''
A hideous way of replacing att values to numerical values only.
'''
def convertValToBinary(formatteddata):
    for line in formatteddata:
        for idx, item in enumerate(line):
            if item == 'N': # non-fatal = 0
                line[idx] = 0
            elif item == 'F' or item == 'Y': # fatal or yes = 1
                line[idx] = 1

            elif item == 'A': # Asian = 1
                line[idx] = 1
            elif item == 'B': # Black = 2
                line[idx] = 2
            elif item == 'L': # Latino = 3
                line[idx] = 3
            elif item == 'O': # Other = 4
                line[idx] = 4
            elif item == 'W': # White/Woman = 0
                line[idx] = 0

            elif item == 'M': # Man = 1
                line[idx] = 1
    return formatteddata

'''
I needed a function to see how many entries are missing values. Returns the
original amount and the amount with missing values.
'''
def checkForMissingData(formatteddata):
    count = 0
    for list in formatteddata:
        if 'U' in list:
            count = count + 1

    return len(formatteddata), count

'''
Some entries contain multiple values for one att. This is to concatenate.
'''
def stringsToInt(formatteddata):
    for line in formatteddata:
        for idx, val in enumerate(line):
            if type(val) == str and val.isdigit():
                line[idx] = int(val)
            if type(val) == str and 'U' in val:
                line[idx] = 'U'
            if type(val) == str and ';' in val:
                if val[0] == 'M' or val[0] == 'm' or val[0] == 'MALE':
                    line[idx] = 1
                if val[0] == 'W' or val[0] == 'w' or val[0] == 'FEMALE' or val[0] == 'F':
                    line[idx] = 0
                if val[0] == 'L' or val[0] == 'l' or val[0] == 'H':
                    line[idx] = 3
                if val[0] == 'A' or val[0] == 'a':
                    line[idx] = 1
                if val[0] == 'B' or val[0] == 'b':
                    line[idx] = 2
                if val[0] == 'O' or val[0] == 'o':
                    line[idx] = 4

    return formatteddata

'''
TO RUN - if running in IDE make sure file name is in your config settings in "parameters"
         if running just in command, make sure txt file is in same folder as CleanData.py
python (or py if in windows) CleanData.py training-uncleaned.txt

IF THAT DOESN'T WORK RUN
python (or py if in windows) -m CleanData.py training-uncleaned.txt

OUTPUT FILE will be called [input file name]-clean.txt i.e. training-clean.txt
'''
def main():
    input = sys.argv[1]
    output_name = input[0:input.index("-")]
    output_name = output_name + "-clean.txt"
    clean(input, output_name)

if __name__ == "__main__":
    main()