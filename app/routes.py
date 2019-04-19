from app import app
import os
from flask import render_template, request, flash, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
from config import Config

#from scripts.plant_and_segment_classes import Segment

def allowed_file(filename):
    if filename.rsplit('.', 1)[1].lower() == 'csv':
        return filename
    else:
        return False

@app.route('/', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #here, i will load the csv into the microplants scripts
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('file_downloads'))
        if not allowed_file(file.filename):
            flash("Incorrect file type. Must be .csv")
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/file-downloads/')
def file_downloads():
	try:
	    return render_template('download.html')
	except Exception as e:
	    return str(e)

#@app.route('/return-files/')
#def return_file():
#    try:
#       return send_file(filename)
 
