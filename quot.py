from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
app = Flask(__name__)
  
@app.route("/",methods=['GET'])
def quot():
    text_file = open('inspiration.txt', "r")
    data = text_file.read().split('\n')
    randomNumber = randint(0,len(data)-1) 
    quote = data[randomNumber] 
    return render_template('test.html',**locals())
