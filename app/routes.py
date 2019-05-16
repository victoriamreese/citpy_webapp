from app import app
import os
from flask import render_template, request, flash, redirect, url_for, send_from_directory


from scripts.cleaning_script import clean_data

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
            df = clean_data(file) 
            filename = 'cleaned_classifications.csv'
            file = df.to_csv((os.path.join(app.config['UPLOAD_FOLDER'], filename)), index=False)
            return redirect(url_for('file_downloads', filename=filename))
        if not allowed_file(file.filename):
            flash("Incorrect file type. Must be .csv")
            return redirect(request.url)
    return render_template('upload.html')


@app.route('/file-downloads/<filename>', methods =['GET'])
def file_downloads(filename):
    if request.method == "GET":
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return render_template('download.html')
