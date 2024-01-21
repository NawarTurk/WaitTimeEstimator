# Source: https://flask.palletsprojects.com/en/3.0.x/
import os
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_session import Session
from werkzeug.utils import secure_filename
from train_model import train_and_get_model, encode_dataframe
from joblib import dump, load
import pandas as pd




# Global model
model = None
part_size = 'PARTY_SIZE'
rank = 'MMR_GROUP_DECILE'
start_time = 'MATCHMAKING_ATTEMPT_START_TIME_UTC'
day = 'MATCHMAKING_DAY_OF_WEEK'
player_role = 'PLAYER_ROLE'
server_name = 'SERVER_NAME'
platform = 'PLATFORM'

g_average = None

"""
File Input Tutorials
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# https://stackoverflow.com/questions/65912720/uploading-and-reading-a-csv-file-with-flask
"""

UPLOAD_FOLDER = 'uploaded_file'
UPLOAD_NAME = "CLIENT_DATASET.csv"
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
  return render_template("index.html")


@app.route("/train", methods=["POST"])
def train():
  # If user is entering data through a form
  if request.method == "POST":
    # Ensure request has files
    if 'file' not in request.files:
      flash('No file part')
      return redirect("/")
    
    file = request.files['file']

    # Ensure user entered a file
    if file.filename == '':
      flash('No selected file')
      return redirect("/")
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      global g_average
      model, error, g_average = train_and_get_model(file)
      print(model, error)

      # Save the trained model to a file
      model_filename = 'trained_model.joblib'
      dump(model, model_filename)
      message= "Trained Model Saved To" + str(model_filename)

      average = "The Average Is: " + str(g_average) "S"

      error = str(round(error,2))
      return render_template("index.html", message="Root Mean Squared Error: " + str(error), average_wait = average)


@app.route("/estimate", methods=["POST"])
def estimate():
  if request.method == "POST":
    # Load the trained model from the .joblib file
    try:
      model = load('trained_model.joblib')
      user_input = {}
      # Assume form validation is complete in javascript, client-side
      user_input[start_time] = int(request.form.get("time")[:2])
      user_input[day] = request.form.get("day")
      user_input[player_role] = request.form.get("role")
      user_input[part_size] = request.form.get("party_size")
      user_input[server_name] = request.form.get("server")
      user_input[platform] = request.form.get("platform")
      user_input[rank] = request.form.get("rank")

      user_df = pd.DataFrame([user_input])
      user_df_encoded = encode_dataframe(user_df)

      estimated_wait = "Estimated Wait Time " + str(round(model.predict(user_df_encoded)[0], 2)) + "S"
      average = "The Average Is " + str(g_average) + "S"


      return render_template("index.html", estimated_wait=estimated_wait, average_wait = average)
    except:
      return render_template("index.html", message="Need to train a model. Please input a csv file.")

    
    
    
  else:
    flash("Must POST")




# Source: https://www.w3schools.com/jquery/
# https://www.w3schools.com/js/
# Import jQuery


"""
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
  
