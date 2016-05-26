
from flask import Flask,render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug import secure_filename
import sys
import os
import subprocess 
import time
import glob

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'JPG', 'PNG'])

#thanks for the help http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/images/wallpapers/<filename>')
def render_image(filename):
	return send_file('images/wallpapers/' + filename, mimetype='image/jpg')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		#return redirect(url_for('uploaded_file', filename = filename))

		subprocess.call(["./imagemaker/imagetest.py", "images/" + filename])
		return render_template('imagePage.html', filename = "/images/wallpapers/" + filename[1:] )
	else:
		return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	subprocess.call(["./imagemaker/imagetest.py", "images/" + filename])
	return render_template('imagePage.html', filename = "/images/wallpapers/" + filename[1:] )


@app.errorhandler(404)
def page_not_found(error):
	return redirect("http://www.columbialion.com", code=302)
	#return redirect(url_for('index')) 
    #return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run()
