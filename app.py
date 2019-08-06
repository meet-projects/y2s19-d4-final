# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/donate')
def donate():
	return render_template('donate.html')
@app.route('/user_guide')
def user_guide():
	return render_template('userguide.html')
@app.route('/user_guide_style')
def user_guide_style():
	return render_template('userguide-style.css')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
