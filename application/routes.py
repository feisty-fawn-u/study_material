from application.__init__ import app 
from application.__init__ import mongo, fs
from flask_pymongo import PyMongo
from gridfs.errors import NoFile
from bson.objectid import ObjectId
from bottle import response
from werkzeug.utils import secure_filename
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session, make_response, abort
#from application.models import User, Course, Enrollment
#from application.forms import LoginForm, RegisterForm
#from flask_restplus import Resource
#from application.course_list import course_list




ALLOWED_EXTENSIONS={'txt','pptx','pdf','png','jpg','jpeg','gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/create', methods=['GET','POST'])
def create():
    if 'file' in request.files:
        file = request.files['file']
        extension = request.form['extension']
        file_name = request.form['file_name']
        print(file)
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            fs.put(filename, content_type=extension, filename=file_name, encoding='UTF-16')
        return 'DONE!'

@app.route('/year')
def year():
    return render_template('year.html')
@app.route('/presentation')
def presentation():
    return render_template('presentation.html')
@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')
    
@app.route('/an')
def am():
    gridout = fs.get(ObjectId("5f0a01f4483e0f2e57ca6206"))
    response = make_response(gridout.read())
    response.mimetype = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    return response
    try:
        grid_out = fs.open_download_stream_by_name("/home/sabreen/Downloads/Tutorial Solution_7.pdf")
        response = make_response(grid_out.read())
        response.mimetype =  "application/pdf"
        return response
    except NoFile:
        abort(404)

    
@app.route('/a', methods=['GET','Post'])
def a():
    if request.method=='POST':
        


    