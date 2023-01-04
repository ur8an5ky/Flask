from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from App.models import User

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    # email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    email_address = EmailField(label='Email', validators=[Email(allow_empty_local=True), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=7), DataRequired()])
    password_confirm = PasswordField(label='Confirm password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('User of that username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('User of that email already exists! Please try a different email address')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
