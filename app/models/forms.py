from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

class UsernameForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])

class PasswordForm(FlaskForm):
    password = PasswordField("password", validators=[DataRequired()])
    confirmation = PasswordField("confirmation", validators=[DataRequired()])

class NameForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])

class EmailForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])

class NewsletterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])

class NewForm(FlaskForm):
    new_type = SelectField("new_type", choices=[("Big Tech", "Big Tech"), ("Opinião", "Opinião"), ("Mobilidade", "Mobilidade"), ("AV/Games", "AV/Games"), ("Inovação", "Inovação"), ("Ciência", "Ciência"), ("Segurança", "Segurança")], validators=[DataRequired()])
    title = StringField("title", validators=[DataRequired(), validators.Length(min=5, max=45)])
    content = TextAreaField("content", validators=[DataRequired()])
    image_path = FileField("image_path", validators=[DataRequired()])
    top = BooleanField("top")