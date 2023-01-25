import csv
from datetime import datetime
import os
import os.path
import pandas as pd
def create ():
    with open (f"contactbook_-{datetime.now():%Y-%m-%d}.csv","a") as book: # creat a csv file with the date of today
        mybook = csv.writer(book)
        if book.tell() == 0: # check that headers are not modifiable 
            mybook.writerow(["Name", "Adress", "Phone Number", "Email Adress", "Insertion time"])
        Name= input("Please enter your name!") 
        Adress=input("Please enter your adress!")
        PhoneNumber=input("Please enter your Phone Number!")
        PhoneNumber= int(PhoneNumber)
        EmailAdress=input("Please enter your Email adress!")
        InsertionTime= now = datetime.now() # insert the date and time of the current moment
        mybook.writerow([Name,Adress,PhoneNumber,EmailAdress,InsertionTime]) # write variables values in the csv file
        my = pd.read_csv("contactbook_-2023-01-25.csv")
        my.loc[13,'Name'] = 'mado' + Adress + PhoneNumber + EmailAdress # update just one variable 
        my.to_csv("contactbook_-2023-01-25.csv", index=False) 
        
create ()

