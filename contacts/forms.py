from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,DateField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from contacts.models import User,Contact



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    secret=StringField('Secret_key',validators=[DataRequired(),Length(min=2,max=10)])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is Already taken!")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email is Already exist!")


class LoginForm(FlaskForm):
    email= StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Sign in')

class addContactForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    pnumber=StringField('Phone Number',validators=[DataRequired(),Length(min=10,max=10)])
    submit=SubmitField('Save')

    def validate_pnumber(self,pnumber):
            user=Contact.query.filter_by(pnumber=pnumber.data).first()
            if user:
                raise ValidationError("PhoneNumber Already exist!")
    
    def validate_email(self,email):
        if email.data!=current_user.email:
            user=Contact.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("email is Already exist!")

class UpdateAccountForm(FlaskForm):
    username=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Submit')

    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username is Already taken!")

    def validate_email(self,email):
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("email is Already exist!")