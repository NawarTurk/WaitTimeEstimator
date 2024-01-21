# Source: https://flask.palletsprojects.com/en/3.0.x/


from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
  """Home Page"""
  # If user is entering data through a form
  if request.method == "POST":
    """
    Data Needed
    """
    user_input = {}
    # Assume form validation is complete in javascript, client-side
    user_input["role"] = request.form.get("role")
    user_input["server"] = request.form.get("server")
    user_input["platform"] = request.form.get("platform")
    user_input["time"] = request.form.get("time")
    user_input["day"] = request.form.get("day")

  else:
    return render_template("index.html")


  
