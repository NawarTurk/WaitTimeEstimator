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
      model, error = train_and_get_model(file)
      print(model, error)

      # Save the trained model to a file
      model_filename = 'trained_model.joblib'
      dump(model, model_filename)
      message= "Trained model saved to" + str(model_filename)

      average = 0

      error = str(round(error,2))
      return render_template("index.html", message="Root Mean Squeared Error: " + str(error), average_wait = average)


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
      print("user encoded")
      print(user_df_encoded)
      print("model prediction")
      print(model.predict(user_df_encoded))

      average = "The average wait time is: " + 100
      estimated_wait = "The estimated wait time is: " + 10

      return render_template("index.html", estimated_wait=estimated_wait, average_wait = average)
    except:
      return render_template("index.html", message="Need to train a model. Please input a csv file.")

  else:
    return render_template("index.html", message="Error: must input form through Post")
