#!/usr/bin/env python


#Created By: Eric Dockery
#Purpose: Programming challenge for Apple CoreOS
#Problem:
#Given a top level directory find all files that have a valid IPv4 address inside
# them, list the files in alphabetical order and the number of IPv4 addresses
    #Sort order
    #numbers
    #Capitals
    #lowercase
#Process:
#OS and sys are needed to traverse files and use terminal commands.
#using OS to traverse all folders and files
#using IPy import IP to check if it is a valid ip address
#check each file line and see if it has
    # a space before it or starts at the beginning of a line
    # has a space after it or finishes at the end of a line
    # Is in the range 0.0.0.0 through 255.255.255.255

#sys for terminal
#os for files/ directories
#operator for 
import os, sys
#save the arg value from the script
arg1 = sys.argv[1]
#determine if the value meets the requirements
def IP(address):
    #counter value works as bool/ int
    counter = 0
    #temp counter
    tempCounter = 0
    #split the potential address by the .'s
    newAddress = address.split('.')
   
    #if this is 4 sets of numbers
    if (len(newAddress) == 4):
        #check each value for correctness
        for eachValue in newAddress:
            
            #make sure it is a digit
            if not eachValue.isdigit():
                tempCounter+=0
            #make sure it is between 0 and 255
            else:
                number = int(eachValue)
                if number <= 0 or number >= 255:
                    tempCounter+=0
                else:
                    tempCounter +=1
    #if all four sections meet the requirements
    if (tempCounter == 4):
        counter = 1
    return counter
            
                    
                
        
def main(arg1):
    #array of words from a line in a file
    wordTestArray = []
    #counter for each files number of IPv4 address
    fileIPCounter =0
    #2D array of file names that have IPv4 addresses and the number of occurances
    filesWithIPv4 =[]
    #for all files, dirs and the root folder
    
    for root, dirs, files in os.walk(arg1):
        #for each file in the folder/ sub folders
        for file in files:
            #open each file ignore .* files
            if not file.startswith('.'):
                with open(root+"/"+file) as f:
                 #read the files line by line and see if it is a valid IPv4
                    for line in f:
                        #this will reset per line
                        wordTestArray = line.split()
                        #look at each word and see if it is IPv4
                        for word in wordTestArray:
                                fileIPCounter +=  IP(word)
                #if file has an IPv4 address
                if (fileIPCounter >0):
                    filesWithIPv4.append([(file), fileIPCounter])
                #reset counter for next file
                fileIPCounter = 0
           
    #after getting array of files with count stored sort
    filesWithIPv4 = sorted(filesWithIPv4, key=lambda x:x[0])
    firstValue =1
    #print the list of values and the number of the IPv4 occurances
    for i in filesWithIPv4:
        if (firstValue ==1 ):
            print(i[0] +" " +str(i[1]))
            firstValue +=1
        else:
            print(i[0] +"," +str(i[1]))
                    
#runs the program            
if __name__=='__main__':
    main(arg1)

            
