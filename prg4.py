#!C:\Program Files\Python39\python.exe

### HTML header for Python script
print("Content-type: text/html \n\n")

# *****************************************************************************
# * SRT211 – Project1 Question 4
# * I declare that this assignment is my own work in accordance with Seneca Academic
# * Policy.
# * No part of this assignment has been copied manually or electronically from any other
# * source (including web sites) or distributed to other students.
# *
# * Name: Anh Dung Phan         Student ID: 123196180   Date: June 26, 2021
# * Name: Ryan Phaphonsomkham   Student ID: 147073167   Date: June 26, 2021
# *
# *****************************************************************************

### Import required libraries/modules
import cgi
import csv

try:
    ### Grab contents of form data and element from HTML page
    form = cgi.FieldStorage()
    a = form.getvalue("file")
    b = form.getvalue("activity")

    ### Open and read the file, then process it with the DictReader method to read the dictionary
    file_name = open(a, 'r')
    csvfile = csv.DictReader(file_name)

    ### Defines start of the HTML table tag and define it's width and border
    print('<table width="" border="">')

    ### Creates an empty dictionary object to store key:value pairs
    form_data = {}
    dict_2 = {}
    
    ### Cycles each row as a key:value pair in the CSV file and stores it in the dictionary object
    for row in csvfile:
        for k, v in row.items():
            try:
                form_data[k].append(v)
            except KeyError:
                form_data[k] = [v]

    #Submission count by StudentID and Rows algorithms
    
    s_id = list(form_data.values())[0] #Get all columns ID
    mark = list(form_data.values())[1:] #Get all columns value
    mark_new = []
    
    #Transpose columns to rows and save in single list
    for i in range(len(mark[0])):
        transpose_mark = []
        for j in range(len(mark)):
            transpose_mark.append(mark[j][i])
        mark_new.append(transpose_mark)   
        
    # Set the Student_ID and value of Student ID on each row into the dictionary keys and values    
    submit_dict = {}
    for i in s_id:
        for j in mark_new:
            submit_dict[i] = j
            mark_new.remove(j)
            break
    
    ### Defines HTML first row and headers
    print("<tr>")
    print("<th>Student ID</th>")
    print("<th>%s</th>" % b)
    print("</tr>")
    
    ### Defines start of HTML second row
    print("<tr>")

    ## Creates a new data row of each Student ID and prints them line by line
    print("<td>")
    for item in form_data['Student ID']:
        print(item)
        print("</br>")
    print("</td>")

    ### Creates a new data row of each activity grade and prints them line by line
    print("<td>") 
    for item2 in form_data[b]:
        print(item2)
        print("</br>")
    print("</td>")
    ### Defines end of HTML second row
    print("</tr>")

    ### Defines end of table
    print('</table>')
    print('<br/>')
    print('<table width="" border="">')
    print("<tr>")
    print("<th>Student ID</th>")
    print("<th>{}</th>".format('No Submission'))
    print("</tr>")
    print("<td>")
    for item in form_data['Student ID']:
        print(item)
        print("</br>")
    print("</td>") 
    
    
    #Submit counts
    print("<td>") 
    for item2 in submit_dict.values():
        count = 0
        #Count the submission
        for j in item2:
            if not j:
                count += 1
        print(count,'/',len(item2))
        print("</br>")
    print("</td>")
    
    print('</table>')


### Exception handling regarding invalid file options
except FileNotFoundError:
    print("File not found, please try again.")
    print('<a href="project_question4.html"><button type="button">Back to Homepage</button></a>')
except:
    print("No file selected.")
    print('<a href="project_question4.html"><button type="button">Back to Homepage</button></a>')