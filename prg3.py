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

#Import library
import cgi
import csv

print('<h1>STUDENT TABLE</h1>')

try:
    #Get the data from HTML form submit with name submit is fname
    form = cgi.FieldStorage()
    a = form.getvalue("fname")
    
    #Open the file and read the file by using csv library
    file = open(a, 'r')
    csvfile = csv.reader(file)
    
    #Create the basic structure of HTML on Python file
    print('<!DOCTYPE html>')
    print('<head>')
    print('<style>')
    print('body {background-color: rgb(255, 255, 204);}')
    print('h1 {color: red;}')
    
    print('#submit {background-color: rgb(153, 255, 102); padding: 15px 32px;}')
    print('</style>')
    print('</head>')
    print('<body>')
    print('<table width="" border="">')
    array = [] #And empty array to store the name of all columns
    
    for i in csvfile: #Loop each value after reading csv file
        array.append(i) #Append the name of columns to empty array above
        print("<tr>") #Create the table and columns
        for j in range(len(array[0])): #Range array[0] is the number of columns
            print("<th>{}</th>".format(i[j])) #With each columns get the specific rows
        print("</tr>")
    print('</table>')
    print('<br/>')
    
    #Create another form action to allow user select some value of columns, 
    #Then submit its to render these columns
    print('<form action="prg3_select.py" method="GET">')
    print('</br>')   
    print('<fieldset>')
    print('<legend><h1>Select Columns</h1></legend>')
    #Array[0][0:] is getting the value of all columns and then using as the name of submit checkbox
    for i in array[0][0:]: 
        print('<input type="checkbox" name="field" id="{}" value="{}" /><label>{}</label><br/>'.format(i, i, i))
    print('</fieldset>')
    
    print('<br/>')
    # The file users chose before.     
    print('<input type="text" value="{}" name="fname"/>'.format(a))
    print('<br/>')
    print('<br/>')
    print('<input type="submit" id="submit" value="Submit"/>')

    print('</form>')
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
    print('</body>')
    print('</html>')
    
    file.close()
#Catch the error and redirect back to home as necessary
except FileNotFoundError:
    print("File not found, Back to enter again")
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
    
    
except:
    print('Nothing !!!')
    print('<a href="prg3.html"><button type="button">Back to Homepage</button></a>')
    
