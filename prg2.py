#!C:\Program Files\Python39\python.exe

### HTML header for Python script
print("Content-type: text/html \n\n")

# *****************************************************************************
# * SRT211 – Project1 Question 2
# * I declare that this assignment is my own work in accordance with Seneca Academic
# * Policy.
# * No part of this assignment has been copied manually or electronically from any other
# * source (including web sites) or distributed to other students.
# *
# * Name: Anh Dung Phan         Student ID: 123196180   Date: June 24, 2021
# * Name: Ryan Phaphonsomkham   Student ID: 147073167   Date: June 24, 2021
# *
# *****************************************************************************

#Import libraries
import cgi
import csv

print('<h1>STUDENT TABLE</h1>')

try:
    #Read data from submit form with fname is filename
    form = cgi.FieldStorage()
    a = form.getvalue("fname")
    #Open the CSV file and using csv library to read the csv file
    file = open(a, 'r')
    csvfile = csv.reader(file)

    print('<body>')
    print('<table width="" border="">')
    array = [] #Empty array to store all columns name
    
    for i in csvfile:
        array.append(i) #Append to empty array above
        print("<tr>")
        for j in range(len(array[0])): #array[0] is all of the columns stored in list
            print("<th>{}</th>".format(i[j])) #From each columns, get the proper rows
        print("</tr>")

    print('</table>')
    print('</body>')
    file.close()
    
#Catch the unwanted error
except FileNotFoundError:
    print("File not found, Back to enter again")
    print('<a href="prg2.html"><button type="button">Back to Homepage</button></a>')
except:
    print("Nothing !!!")
    print('<a href="prg2.html"><button type="button">Back to Homepage</button></a>')
