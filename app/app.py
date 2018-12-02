from flask import Flask, request,render_template
from werkzeug.utils import secure_filename
import os
#from flask_restful import Resource, Api
from flask import jsonify
import PdfToText_WordArray as p1
import classifyRegulatoryDoc as cl_reg
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup_manager.html')

@app.route('/uploaderabhi', methods=['POST'])
def formdata():
        print(request.form['firstname'])
        print(request.form['lastname'])
        print(request.form['email'])
        #print(request.form['email'])
        return "Done"

   


@app.route('/matchdocs')
def match_docs():
    return render_template('match_docs.html')


'''
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file3():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        f1.save(secure_filename(f1.filename))
        f2.save(secure_filename(f2.filename))
        os.rename(str(f1.filename), "file1.pdf")
        os.rename(str(f2.filename), "file2.pdf")
        return getMatchedArray()
'''



@app.route('/uploader1', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f1 = request.files['file1']
        f1.save(secure_filename(f1.filename))
        os.rename(str(f1.filename), "file1.pdf")
        return render_template('match_docs.html')

@app.route('/taxonomy', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f2 = request.files['file2']
        f2.save(secure_filename(f2.filename))
        os.rename(str(f2.filename), "file2.pdf")
        list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
        matchedWords = p1.getMatchedWords(list1,list2)
        return render_template('matched_words.html',matchedWords=matchedWords)
        #return getMatchedArray()
        
@app.route('/dashboard',methods=['GET'])
def dashboard():
    if request.method == 'GET':
        classifiedText = cl_reg.classifyRegDoc("file2.pdf")
        return render_template('dashboard.html',classifiedText = classifiedText,count_texts=cl_reg.count_texts)


def getMatchedArray():
    matchedWords = []
    list1,list2 = p1.createWordArray("file1.pdf","file2.pdf")
    matchedWords = p1.getMatchedWords(list1,list2)
    return jsonify(matchedWords)

if __name__ == '_main_':
    app.run()