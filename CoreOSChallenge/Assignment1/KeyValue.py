#!/usr/bin/env python


#Created By: Eric Dockery
#Purpose: Programming challenge for Apple CoreOS
#Problem:
#Assume a file has the following entries. The first column contains the key and the second column contains
#the value(s). The first line X1 is the key with X2, X3, and X4 as values.
#X1   X2,X3,X4
#X2   X4,X5
#X3   X6,X7
#X4  1,2,3
# This Program will take an input value (a key) and print the values for the key. 
# Example:
#X4---->1--->2---3
#Also it will print the dependencies for example X2 will show:
#X2----->X4---->1--->2--->3---->X5
#The order of the values do not matter.
#It should function with any number of keys/values.

#Process:
#My thought process is that this should be best created using the python dictionary. Since it will need to have keys and values.
#the fun part of this program is that the first value is not comma seperated from the others meaning that some of the
#built in functions for parsing data like this will not work. Recursion is most likely
#the best solution. 


#format for file input set to filename keyValue

import sys
#arguments - global
arg1 =sys.argv[1]
arg2 = sys.argv[2]
#call and test if value has a key
def SubKey(dictionary, value, finList):
    try:
        for key in dictionary[value]:
            #test if the value is also a key and if so follow its child
            finList.append(key)
            if key in dictionary:
                SubKey(dictionary, key, finList)
    except:
        key = 0

def main(fileName, keyValue):
    #establish the dictionary for the key/values
    dictionary ={}
    #set up the text for key To Key/ key To First Value
    keyToValue = "---->" #works as valueToKey as well
    keyToKey = "----->"
    #value to value in key or value to key
    valueToValue ="--->"
    #value to last value
    valueToLastValue = "---"
    #Final parse list
    finList = []
    #string to print at the end
    stringToPrint = keyValue 
    #first open the file and store the data
    with open(fileName) as f:  #with handles opening and closing of file and exceptions 
        for line in f:         #buffered I/O and memory managment so size won't be an issue
            lineSplitArray = line.split() #parse each line into an array split by the key and values
            lineValueArray = lineSplitArray[1].split(",")  #get an array of each value
            #add the key and values
            dictionary[lineSplitArray[0] ]= [] #sets the key values for the dictionary
            for value in lineValueArray:
                dictionary[lineSplitArray[0]].append(value)#adds the line values to the dictionary key
    #after the file is finished being read and data is stored to the dictionary
    #finList will have all values including duplicates              
    finList.append(SubKey(dictionary, keyValue, finList))
    #using set to remove duplicates
    uniqueList = set(finList) #will put in order of None, values,..., Keys
    #use a lambda to remove None quickly and memory managed
    uniqueList = [x for x in uniqueList if x is not None]
    #due to sort the first value will always be an int.
    #structure for loop and if statements for that because of no switches in python        
    for thisValue in uniqueList:
        #if the value is the same as the starting value we should ignore it
        if (thisValue == keyValue):
            stringToPrint =stringToPrint
        else:
            #if we are at the first value
            if(uniqueList.index(thisValue) == 0):
            
                #if the first value is a key
                if(thisValue.startswith("X")):
                    stringToPrint += (keyToKey+thisValue)
                #elif it is int and not the last value
                elif(uniqueList.index(thisValue)+1 != len(uniqueList)):
                    stringToPrint +=(keyToValue+thisValue)
                    #lastValue to be used for middle comparisions
                    lastValue =thisValue
                #if it is int and last value
                else:
                    stringToPrint += (valueToLastValue+"-"+thisValue)
                    
                    
            #not first but not last           
            elif(uniqueList.index(thisValue)+1 != len(uniqueList)):
                #set the nextValue for comparision of key to key values
                #if last key to new key
                if (lastValue.startswith("X") and thisValue.startswith("X")):
                    stringToPrint += (keyToKey+thisValue)
                #else value to key
                elif(thisValue.startswith("X")):
                    stringToPrint += (keyToValue+thisValue)
                #else int to int
                else:
                    stringToPrint += (valueToValue+thisValue)
    
                lastValue = thisValue
            #end of values
            else:
                if (thisValue.startswith("X")):
                    stringToPrint += (keyToValue+thisValue)
                #else it is int, but we need to make sure its not the last int 
                else:
                    stringToPrint += (valueToLastValue+thisValue)
    #print the final results
    print(stringToPrint)
            



#runs the program            
if __name__=='__main__':
    main(arg1, arg2)
    
