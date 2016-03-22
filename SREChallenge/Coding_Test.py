#Programmed by: Eric Dockery
#Date: 11/21/2015
#Purpose: Site Reliability Engineer Exercise
#Challenge:
#   Write a Python program that opens file 'data.csv'
#   Sorts data by price
#   Prints the result to standard out

#imports
import csv
import operator
import os
import time
#Main program

def main():
    #obtain filename - commented out due to only needing the data.csv
    ##fileName = input("What data file do you want to see? ")
    fileName = "data.csv"
    #open filename
    openFile = open(fileName)
    #use csv import DictReader - this works like a generator - stores all values in a dictionary
    # that has keyword and value
    dataFromFile=csv.DictReader(openFile)
    
    #the default function sorted in the operator function takes in the csv data
    # and finds the keyword that we want to sort, then if you want it in accending or
    #decending order
    sortedlist = sorted(dataFromFile, key=lambda d:float(d['DISCOUNTED_PRICE']), reverse= True)
    openFile.close()
    #write the data back to a temp csv
    tempWrite = open('output.csv', 'w')
    writer = csv.DictWriter(tempWrite, dataFromFile.fieldnames)
    writer.writeheader()
    writer.writerows(sortedlist)
    tempWrite.close()
    #need to wait until it is finished writing
    while not os.path.exists('output.csv'):
        time.sleep(1)
    #open temp file
    tempFile = open("output.csv", "r")
    FinishedData = csv.reader(tempFile)
    #prints the output to stdout
    for row in FinishedData:
        print(row)
    tempFile.close()
    #Comment to keep the csv file if needed
    os.remove('output.csv')
    try:
        raw_input()
    except:
        print("")
main()
