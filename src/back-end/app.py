import os
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect
from werkzeug.utils import secure_filename
from csim import *

app = Flask(__name__)
app.config['Extension'] = ('.pdf', '.txt', '.html') # Acceptable extension for uploaded file
app.config['ExtensionS'] = ('*.pdf', '*.txt', '*.html') # File extension for returning search
app.config['Path'] = '../../test/' # Path to documents folder (relative to current app.py)
app.config['Query'] = 'query' # Parameter from reactjs

@app.route('/upload', methods=['POST','GET']) # Route to upload file
def upload_files():
    if request.method == "POST":
        upDoc = request.files["file"]
        upDocName = secure_filename(upDoc.filename) # Secure a file name
        print(upDoc)
        if upDocName != '': # Filename is legal
            if not upDocName.lower().endswith(app.config['Extension']): # Checking file extension
                return 'File extension not allowed'
            upDoc.save(os.path.join(app.config['Path'], upDocName)) # Upload to documents folder
        else : # Illegal file name
            return 'File name error!'
        return 'File Uploaded!' 

@app.route('/database/<filename>',methods=['GET']) # Route to return file
def view_file(filename):
    if isfilenotempty(app.config['Path'],filename): # Check if file is not empty
        return send_from_directory(app.config['Path'], filename) # File is not empty and returned to be shown
    return redirect('/error/emptyfile') # File is empty and redirect to route /error/emptyfile

@app.route('/error/emptyfile',methods=['GET']) # Route to redirect error : empty file
def errorq(): 
    return 'ERROR : FILE IS EMPTY' # Return a error message

@app.route('/search/',methods=['POST','GET']) # Route to search query
def search():
    query = request.get_json() # Get query from reactjs
    return jsonify(searchq(query[app.config['Query']],app.config['Path'],app.config['ExtensionS'])) # Return array of dict

@app.route('/table',methods=['POST','GET']) # Route to search result table
def table():
    query = request.get_json() # Get query from reactjs
    return jsonify(searchqt(query[app.config['Query']],app.config['Path'],app.config['ExtensionS'])) # Return table in form of array [[..],[..],..,[..]]