#!C:\Program Files\Python39\python.exe

### HTML header for Python script
print("Content-type: text/html \n\n")

# *****************************************************************************
# * SRT211 – Project1 Question 3
# * I declare that this assignment is my own work in accordance with Seneca Academic
# * Policy.
# * No part of this assignment has been copied manually or electronically from any other
# * source (including web sites) or distributed to other students.
# *
# * Name: Anh Dung Phan         Student ID: 123196180   Date: June 25, 2021
# * Name: Ryan Phaphonsomkham   Student ID: 147073167   Date: June 25, 2021
# *
# *****************************************************************************

import cgi
import csv

print('<h1>TABLE SELECTED</h1>')

try:
    #Read the submit data from SECOND form in prg3.py with name are fname and field
    form = cgi.FieldStorage()
    dataFile = form.getvalue("fname")
    dataField = form.getvalue("field")
    
    #When we have multiple columns selected (query), it stores on the array
    #However 1 column selected, it is a string. If condition help store any 
    #columns selected into 1D array
    if type(dataField) == str:
        dataField = list([dataField])
    
    #Read the file1.csv or file2.csv via the fname submitted
    file = open(dataFile, 'r')
    csvfile = csv.reader(file)
    print('<!DOCTYPE html>')
    print('<head>')
    print('<style>')
    print('body {background-color: rgb(255, 230, 230);}')
    print('button {background-color: rgb(102, 194, 255); padding: 15px 32px;}')
    print('h1 {color: Green;}')
    print('</style>')
    print('</head>')
    print('<body>')
    print('<table width="" border="">')
    print('<body>')
    print('<table width="" border="">')
    array = [] #Empty array to store the list of value on table
    
    for i in csvfile:
        # Append into the empty list above
        array.append(i)
        #Create the table with ixj columns and rows (matrix)
        print("<tr>")
        for j in range(len(dataField)): #dataField are the columns selected and store in array on line 17
            if dataField[j] in array[0]: #If each value on dataField exists on the array (all columns)
                #Get index of this each dataField value within array 
                c = array[0].index(dataField[j])
                print('<th>{}</th>'.format(i[c])) #Display the suitale data
        print("</tr>")
          
    print('</table>')
    print('<br/>')
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
    print('</body>')
    print('</html>')
    
    file.close()
#Try catch the errors and redirect to home page if user press button
except FileNotFoundError:
    print("File not found, Back to enter again")
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
except Exception as e: 
    print("Nothing !!!")
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
