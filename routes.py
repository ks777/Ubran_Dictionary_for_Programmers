from flask import Flask, url_for, render_template, request
from app import app

import pymysql, string
    
#first page
@app.route('/')
def commence():
    #expect to make an html file for the first page like the rest.
    return render_template('hackprinceton.html')

@app.route('/complete', methods = ['GET','POST'])
def create():
    new_str = ''
    off = 0
    if request.method == 'GET':
        if off == 0:
            return render_template('hackprinceton.html')
    if request.method == 'POST':
        conn = pymysql.connect(host='localhost', port = 3306, user = 'root', passwd = 'hello', database = 'pinhead')
        cursor = conn.cursor()
        words = cursor.execute("SELECT original, simplified FROM pinhead.terming2")
        x = request.form['title']
        x = x.lower()
        y = x
        if x == "c#":
            x = x
        elif x == "c++":
            x = x
        else:
            x = ''.join(c for c in x if c.isalpha() or c.isspace())

        for i in range(cursor.rowcount):
            row = cursor.fetchone()
            if row[0] in x:
                new_str = str.replace(x, row[0], row[1])
                x = new_str
                off = 1
                
                
        if off == 1:
            return render_template('hackfinished.html', x = x, y = y)
        elif off == 0:
            return render_template('anewhack.html')
    cursor.close()
    conn.close()
    
@app.route('/wondering', methods = ['GET','POST'])
def man():
        conn = pymysql.connect(host='localhost', port = 3306, user = 'root', passwd = 'hello', database = 'pinhead')
        cursor = conn.cursor()
        words = cursor.execute("SELECT original, simplified FROM pinhead.terming2")
        w = request.form['ask1']
        z = request.form['ask2']
        cursor.execute("INSERT INTO terming2 VALUES (%s,%s)",(w, z))
        conn.commit()

        return render_template('anewhackfinish.html',w = w, z = z)
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


#aws/domain name
#transfer work,submit via devpost, and check if work is workable in laptop


