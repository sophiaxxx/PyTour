from flask import render_template

def index():
    title = "Welcome to Chu's Space"
    big_word = "A little time with myself"
    return render_template('index.html', title=title, big_word=big_word) 

def hello_world():
    return "Hello, how are you?"

