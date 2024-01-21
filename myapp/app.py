# Source: https://flask.palletsprojects.com/en/3.0.x/
import csv
import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'uploaded_files'
ALLOWED_EXTENSIONS = {'csv'}

# Configure application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
  """Home Page"""
  # If user is entering data through a form
  if request.method == "POST":
    # Ensure request has files
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    
    file = request.files['file']

    # Ensure user entered a file
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      # Assume friendly user
      return redirect("index.html")

    # https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
    # https://stackoverflow.com/questions/65912720/uploading-and-reading-a-csv-file-with-flask

    user_input = {}
    # Assume form validation is complete in javascript, client-side
    user_input["role"] = request.form.get("role")
    user_input["server"] = request.form.get("server")
    user_input["platform"] = request.form.get("platform")
    user_input["time"] = request.form.get("time")
    user_input["day"] = request.form.get("day")

    # Ensure they inputted a file
    # Ensure user inputted a .xlsx file
    # Ensure it has the correct headers
    #filename == 'data/testdata.xlsx':

  else:
    return render_template("index.html")



"""
# Source: https://www.w3schools.com/jquery/
# https://www.w3schools.com/js/
# Import jQuery
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("p").click(function(){
    // Validate form
    if validated:
      # Send to form
      $("#answer1").text(wait_time);
  
  });
});

</script>
"""
  
