"""
 Name: Hannah Siitia, My Linh Quach, Adrienne Slawik
 NOTE: ALL WORKED TOGETHER ON SAME MACHINE BEFORE MOVING TO GIT
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: October 15th,2021
 Sources consulted: Reviewed slides on using pickle

 Known Bugs: N/A, only edited main function to explain what files will be called.
 Run same as original.

 Creativity: n/a

 Instructions: Run same as original.

"""
import sys
import argparse
import math
import pickle
import random

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    index = 0
    num_lines = sum(1 for line in open(data, encoding="UTF-8"))
    fandnfpolicedata = [0] * num_lines

    with open(data, encoding="UTF-8") as file:
        for line in file:
            fandnfpolicedata[index] = line
            index += 1

    fandnfpolicedata.pop(0)
    trainingamount = int(len(fandnfpolicedata) * ratio)
    trainingdata = fandnfpolicedata[0:trainingamount]
    testingdata = fandnfpolicedata[trainingamount+1:len(fandnfpolicedata)]

    with open(trainData, "w", encoding="UTF-8") as file:
        for case in trainingdata:
            file.write(str(case))
        file.close()

    with open(testData, "w", encoding="UTF-8") as file:
        for case in testingdata:
            file.write(str(case))
        file.close()

def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    index = 0
    num_lines = sum(1 for line in open(data, encoding="UTF-8"))
    fandnfpolicedata = [0] * num_lines

    with open(data, encoding="UTF-8") as file:
        for line in file:
            fandnfpolicedata[index] = line
            index += 1

    fandnfpolicedata.pop(0)
    random.shuffle(fandnfpolicedata)
    trainingamount = int(len(fandnfpolicedata) * ratio)
    trainingdata = fandnfpolicedata[0:trainingamount]
    testingdata = fandnfpolicedata[trainingamount+1:len(fandnfpolicedata)]

    with open(trainData, "w", encoding="UTF-8") as file:
        for case in trainingdata:
            file.write(str(case))
        file.close()

    with open(testData, "w", encoding="UTF-8") as file:
        for case in testingdata:
            file.write(str(case))
        file.close()

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode

    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    #random Splitting
    if(mode == "R"):
        splitDataRandom("police-data.csv", "training-data.txt", "test-uncleaned.txt", 0.7)

    #normal Splitting
    if(mode == "N"):
        splitData("police-data.csv", "training-data.txt", "test-uncleaned.txt", 0.7)

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    # your code here
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting. Check training-data,txt and test-uncleaned.txt for results')
    if len(sys.argv)<3:
        showHelper()
    main()
