from flask import  Flask, render_template		# importing the Flask instance from the entire Flask package
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)           # Initialize the instance of the flask with the given argument
# 								# __name__ refers to the local python file I am working with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slotdata.db'
db = SQLAlchemy(app)			# initializing the class
app.config['SECRET_KEY'] = '2c18235be4c572e07c1cc56e'


from slotinfo import routes
