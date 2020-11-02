import imghdr
import os
from flask import Flask, render_template, request, send_from_directory,jsonify
from werkzeug.utils import secure_filename
from csim import *

app = Flask(__name__)
app.config['Extension'] = ('.pdf', '.txt', '.html')
app.config['ExtensionS'] = ('*.pdf', '*.txt', '*.html')
app.config['Path'] = '../test/'

# @app.route('/')
# def index():
#     dir = os.listdir(app.config['Path'])
#     return render_template('index.html',files=dir)

@app.route('/upload', methods=['POST'])
def upload_files():
    upDoc = request.files['upDoc']
    upDocName = secure_filename(upDoc.filename)
    if upDocName != '':
        if not upDocName.lower().endswith(app.config['Extension']):
            return 'File extension not allowed'
        upDoc.save(os.path.join(app.config['Path'], upDocName))
    else : 
        return 'File name error!'
    return 'File Uploaded!'

@app.route('/database/<filename>',methods=['POST']) # return file
def view_file(filename):
    return send_from_directory(app.config['Path'], filename)

# @app.route('/search')
# def searcht():
#     return render_template('search.html')

@app.route('/search/',methods=['POST'])
def search():
    query = request.args.get('query')
    return(jsonify(searchq(query,app.config['Path'],app.config['ExtensionS'])))