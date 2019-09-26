from flask import Flask,render_template
from flask_wtf import Flask_Form
from wtforms import StringField,PasswordField

app=Flask(__name__)
app.config['SECRET_KEY]

