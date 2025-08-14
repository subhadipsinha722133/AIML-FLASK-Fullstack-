from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,Length



class RegistrationForm(FlaskForm) :
    name = StringField("Full Name", validators=[DataRequired(message="Name is required" )])
    email = StringField("Email",validators=[DataRequired(message="Email is required"), Email(message="Invalid Email")])
    password = PasswordField("Password", validators=[DataRequired(message="Password is requred"), Length(min=6,message="Password must be at least 6 characters long")])

    submit = SubmitField("Register")

