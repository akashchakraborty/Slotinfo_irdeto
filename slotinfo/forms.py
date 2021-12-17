from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SubmitField, SelectField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TelField
from wtforms.validators import DataRequired

projects=["Navya 1.5","Navya 1.6","Navya 1.8","Navya 3","Prithvi","AirtelPHD Zapper","Airtel PVRLite",
        "AIT 3.0"]

class RegisterForm(FlaskForm):
    first_name = StringField(label='First Name:')
    last_name = StringField(label='Last Name:')
    email_address = StringField(label='Email Address:')
    current_address = TextAreaField(label='Your current adress details')
    password1=PasswordField(label='Password:')
    password2=PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Submit')


class ReserveForm(FlaskForm):
    racks=[1,2,3,4]
    slots=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    global projects
    name = StringField(validators=[DataRequired()],label="Name: ")
    rack = SelectField(validators=[DataRequired()],label="Rack: ",choices=[i for i in racks])
    slot = SelectField(validators=[DataRequired()],label="Slot: ",choices=[i for i in slots])
    days = IntegerField(label="Number of days: ")
    projectname = SelectField(validators=[DataRequired()],label="Project Name: ")
    reserve = SubmitField(label='Reserve')
    desc = TextAreaField(validators=[DataRequired()],label="Details: ")