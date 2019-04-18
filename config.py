import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    UPLOAD_FOLDER ='/uploads'    
    ALLOWED_EXTENSIONS = set('csv')
    
