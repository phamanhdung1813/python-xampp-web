# *****************************************************************************
# * SRT211 – Project1 Question 1
# * I declare that this assignment is my own work in accordance with Seneca Academic
# * Policy.
# * No part of this assignment has been copied manually or electronically from any other
# * source (including web sites) or distributed to other students.
# *
# * Name: Anh Dung Phan         Student ID: 123196180   Date: June 24, 2021
# * Name: Ryan Phaphonsomkham   Student ID: 147073167   Date: June 24, 2021
# *
# *****************************************************************************

# Import the library Pandas and NumPy
import pandas as pd
import numpy as np

try:
    path1 = ('file1.csv') #The path to the csv file
    df1 = pd.read_csv(path1) #Pandas with read_csv() uses to open the file and read the file.
    student_id_1 = np.array(df1['Student ID']) #NumPy array uses to select the column Student ID

    path2 = ('file2.csv') #The path to the csv file
    df2 = pd.read_csv(path2) #Pandas with read_csv() uses to open the file and read the file.
    student_id_2 = np.array(df2['Student ID']) #NumPy array uses to select the column Student ID

    exist_both = [] #Create empty array to append Student IDs who exist on both courses
    not_exist_both = [] #Create empty array to append Student IDs who not exist on both courses

    # The program append the Student ID on both course to these empty above
    for i in student_id_1:
        if i in student_id_2:
            exist_both.append(i)
        else:
            not_exist_both.append(i)
    
    # Display the result:        
    print("Student ID exist in both courses are:\n ")
    print(exist_both)

    print('\n')

    print("Student ID not exist in both courses are:\n ")
    print(not_exist_both)
except FileNotFoundError: #Catch the error when the file is not currently exist
    print('File is not exist on your folder')
except: # Final catch error
    print('Finally nothing !!!')
    