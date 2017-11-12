#<input type = '<type>' name = '<name>' />

from flask import Flask, url_for, request, render_template
from app import app

@app.route('/')
def commence():
    #expect to make an html file for the first page like the rest.
    return render_template('hackprinceton.html')
