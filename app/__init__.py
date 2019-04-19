from flask import Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

from app import routes


