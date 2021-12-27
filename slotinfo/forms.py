from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SubmitField, SelectField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TelField
from wtforms.validators import DataRequired

projects=["Navya 1.5","Navya 1.6","Navya 1.8","Navya 3","Prithvi","AirtelPHD Zapper","Airtel PVRLite",
        "AIT 3.0"]

class AddProjectForm(FlaskForm):
    projectname = StringField(validators=[DataRequired()],label="Project Name: ")
    submit_proj = SubmitField(label='Add Project')