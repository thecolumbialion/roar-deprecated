
from flask import Flask,render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug import secure_filename
import sys
import os
import subprocess 
import time
import glob

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg'])

#thanks for the help http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/images/wallpapers/<filename>')
def render_image(filename):
	return send_file('images/wallpapers/' + filename, mimetype='image/jpg')

@app.route('/')
def index():
	#return 
	#print("hi")
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	#return 
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#time.sleep(1)
		return redirect(url_for('uploaded_file', filename = filename))
	else:
		return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	subprocess.call(["./imagemaker/imagetest.py", "images/" + filename])
	#time.sleep(0.01)
	

	#path = "/images/wallpapers/"
	#os.chdir(path)
	#files = sorted(os.listdir(path), key=os.path.getmtime)
	#newest = files[-1]
	#print(newest)
	#newest = max(glob.iglob('*.[pj][np]g'), key=os.path.getctime)
	#newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)
	return render_template('imagePage.html', filename = "/images/wallpapers/" + filename[1:] );
@app.route('/download/<filename>', methods=['POST'])


	"""print("testing here")
	if request.method == 'POST':
		f.request.files['input']
		f.save("../images/background.png")
    	return render_template('index.html')"""



"""@app.route('/makeimage')
def imageMaker():
	subprocess.call("../imagemaker/imagetest.py")
	time.sleep(5)

	#maybe add a temporary site that just says loading while waiting
	#render_template("")
	return render_template('../newImage/index.html')"""



@app.errorhandler(404)
def page_not_found(error):
	return "Heading to The Lion's Website..." and redirect("http://www.columbialion.com", code=302)
	return redirect(url_for('index')) 
    #return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run()
