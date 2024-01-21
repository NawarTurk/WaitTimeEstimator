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
    # Ensure user submitted the form
    if request.form

  
