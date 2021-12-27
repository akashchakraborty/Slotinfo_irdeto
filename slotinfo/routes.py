from slotinfo import app
from flask import render_template,request,redirect
from slotinfo.models import Item
from slotinfo.models import Projects
from slotinfo.forms import AddProjectForm
from slotinfo import db
from slotinfo.models import Projects

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
	form = AddProjectForm()
	return render_template('home.html',form=form)

@app.route('/rack1')
def rack_one():
	items = Item.query.filter_by(rack_number=1)
	form = AddProjectForm()
	return render_template('rack1.html',items=items,form=form)

@app.route('/rack2')
def rack_two():
	items2 = Item.query.filter_by(rack_number=2)
	form = AddProjectForm()
	return render_template('rack2.html',items=items2,form=form)

@app.route('/rack3')
def rack_three():
	items3 = Item.query.filter_by(rack_number=3)
	form = AddProjectForm()
	return render_template('rack3.html',items=items3,form=form)

@app.route('/witbe1')
def wit_rack1():
	items4 = Item.query.filter_by(rack_number=4)
	form = AddProjectForm()
	return render_template('rack4.html',items=items4,form=form)

@app.route('/addproject', methods=['GET','POST'])
def add_project():
	form = AddProjectForm()
	name=form.projectname
	name2 = request.form['projectname']
	x=Projects(projname=name2)
	db.session.add(x)
	db.session.commit()
	return redirect(request.referrer)

# @app.route('/signup/official')
# def signup_page1():
# 	form = OfficialForm() # creates the form object 
# 	return render_template('official_signup.html',form=form)
