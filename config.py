import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret'
    UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'    
    DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
    ALLOWED_EXTENSIONS = set('csv')
