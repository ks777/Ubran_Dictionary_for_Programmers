
from flask import Flask, url_for, render_template
from app import app

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
