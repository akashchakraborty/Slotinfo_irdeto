from slotinfo import app
from flask import render_template
from slotinfo.models import Item
from slotinfo.forms import ReserveForm


# @app.route('/')					# The decorator which specifies the url we are going to navigate to

# def hello_world():
	# return "<h1>Hello World, But Bigger Version !!! </h1>"

@app.route('/about') 			# thus the function can give changes to http://127.0.0.1:5000/about
def about_page():
	return render_template('about.html')


# @app.route('/about/<username>') # dynamic routing instead of hardcoding the route
# def about_page(username):
# 	return "<h1>About Page of {}".format(username)

@app.route('/')	
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/rack1')
def rack_one():
	items = Item.query.filter_by(rack_number=1)
	return render_template('rack1.html',items=items)

@app.route('/rack2')
def rack_two():
	items2 = Item.query.filter_by(rack_number=2)
	return render_template('rack2.html',items=items2)

@app.route('/rack3')
def rack_three():
	items3 = Item.query.filter_by(rack_number=3)
	return render_template('rack3.html',items=items3)
# @app.route('/signup/official')
# def signup_page1():
# 	form = OfficialForm() # creates the form object 
# 	return render_template('official_signup.html',form=form)
