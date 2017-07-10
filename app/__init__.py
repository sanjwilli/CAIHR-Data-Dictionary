from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATA_DICTIONARY_FOLDER = './app/Data Dictionary'

app = Flask(__name__)
app.config.from_object(__name__)

from app import views