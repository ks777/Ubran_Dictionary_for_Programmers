#from flask import Flask, url_for, render_template
#from app import app

import pymysql, string
    
new_str = ''
off = 0
x = input("please enter a sentence so i can dumb it down for you: ")
x = x.lower()
if x == "c#":
    x = x
    print(x)
elif x == "c++":
    x = x
    print(x)
else:
    x = ''.join(c for c in x if c.isalpha() or c.isspace())
    print(x)
    
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', passwd = 'hello', database = 'pinhead')
cursor = conn.cursor()
words = cursor.execute("SELECT original, simplified FROM pinhead.terming2")
#finally finds the value, but must be very specific
#currently only works for 1 call, need to work for multiple


for i in range(cursor.rowcount):
    row = cursor.fetchone()
    if row[0] in x:
        new_str = str.replace(x, row[0], row[1])
        x = new_str
        print(new_str)
        off = 1
print(x)


while off == 0:
    y = input("The word does not seem to be in our database...yet! Place the word you want to give meaning here: ")
    z = input("Write a description of the word! Be sure to simplify it as much as you can: ")
    cursor.execute("INSERT INTO terming2 VALUES (%s,%s)",(y, z))
    conn.commit()
    print("congrats! you just added a new term!")
    off = 1
    break

#c, c#, and c++ act differently and print out twice. make sure you take this into account

#9 pm checkup
#html
#aws
#rewrite the database
#MOST OF THE BACKEND IS FINISHED! NOW DO THE DATABASE AND WORK ON THE HTML/FLASK
        

cursor.close()
conn.close()


    
#main point of the program:
#user will input sentence, program will output "simplified" version
#in the case that the word does not exist in the database, program should ask
#user to input new response, and with a click, should be able to update.

#so what i need to do now is make sure what the program checks is the new words
#or rather, think about it like this:
#it just replaces the designated words if it finds it
#so there should be two user inputs: the word and the new word
#need to figure out how to put word and new word into the database/list

#NEEDS TO BE A DATABASE TO BE CONTINUOUSLY KEEPING THE UPDATES




