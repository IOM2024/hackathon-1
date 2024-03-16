# Python Conditional Statements 




# Create a Python program that:


# - Prompts a user to enter their age
Full_name=input("Enter your full names:")
age=int(input("Enter your age:"))
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
if age>18:
    print("Hello,%s,youre %d years old.You are eligible to vote"%(Full_name,age))
elif age == 18:
    print("Hello, %s, you're %d years old. You can now start voting." % (Full_name, age))
else:
    print("Hello, %s, you're %d years old. You are not eligible to vote." % (Full_name, age))

#IN MY PROGRAM THERE IS NO CHECKING VOTING AGE LIMITS. 
#THEREFORE WE CAN ESTIMATE THE TIME TAKEN FOR EACH SUCCESIFULL CHECKING IN SECONDS.
#Let us numpy array to correct and present this data
import numpy as np
import pandas as pd
#let us assume that the program recorded the name and respective age
names={
    "Gladys":17, "Innocent":21, "Kevo":15, "Alan":18
}
#let us make a small data seies
DatS=pd.Series(names)
print(DatS)
print()
#calculate std,mean,max,count......
print("Description")      
print(DatS.describe())
#IN MY PROGRAM THERE IS NO CHECKING VOTING AGE LIMITS. 
#THEREFORE WE CAN ESTIMATE THE TIME TAKEN FOR EACH SUCCESIFULL CHECKING IN SECONDS.
#Let us numpy array to correct and present this data
# time 
timein_minsecs = np.random.rand(6,4)

# Names of individual who we want to analyse
Innocent = ["Login1", "Login2", "Login3", "Login 4"]

# Estimate the date and time they checked if they can vote
date = pd.date_range("today", periods=6)[::-1]

# Creating a DataFrame using pandas
Inno_data= pd.DataFrame(timein_minsecs, index=date, columns=Innocent)

print(Inno_data)

print()
#calculate std,mean,max,count......      
print(Inno_data.describe())



    