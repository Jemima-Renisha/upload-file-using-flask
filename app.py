from flask import Flask, request, render_template, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if file is selected
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('File uploaded successfully')
            return redirect(request.url)
        else:
            flash('This file is not supported, upload only png, pdf, txt, jpeg, jpg, gif extension files')
            return redirect(request.url)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
