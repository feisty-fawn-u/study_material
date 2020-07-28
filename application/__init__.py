from flask import Flask 
from config import Config 
from application import routes
from pymongo import MongoClient 
import gridfs
from gridfs import GridFSBucket


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
client = MongoClient('mongodb://127.0.0.1:27017')


mongo=client.study_material
#fs=gridfs.GridFS(mongo)
fs= GridFSBucket(mongo)