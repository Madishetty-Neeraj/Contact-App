import os
import secrets
from turtle import title
from flask import render_template,url_for,flash,redirect,request
from contacts import app,db,bcrypt
from contacts.models import User,Contact
from contacts.forms import LoginForm,RegistrationForm,addContactForm,UpdateAccountForm
from flask_login import login_user,current_user,logout_user,login_required



@app.route("/",methods=['GET'])
@app.route("/home",methods=['GET'])
def home():
    contacts=Contact.query.filter_by(user_id=current_user.get_id())
    return render_template("home.html",title='Home',contacts=contacts)


@app.route("/signUp",methods=['GET','POST'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password,secret=form.secret.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created !','success')
        return redirect(url_for('login'))
    return render_template('signUp.html',title='SignUp',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('SignIn unsuccessful.please check ur email and password','danger')
    return render_template('signIn.html',title='signIn',form=form)


@app.route("/logout",methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/addcontact",methods=['GET','POST'])
def addcontact():
    form=addContactForm()
    if form.validate_on_submit():
        new=Contact(name=form.name.data,email=form.email.data,pnumber=form.pnumber.data,user_id=current_user.get_id())
        db.session.add(new)
        db.session.commit()
        flash(f'contact added successfully !','success')
        return redirect(url_for('addcontact'))
    contacts=Contact.query.filter_by(user_id=current_user.get_id())
    return render_template('addContact.html',title='New Contact',form=form,contacts=contacts)

    
@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated!','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data =current_user.username
        form.email.data=current_user.email
    return render_template('account.html',title='Account',form=form) 






































    



         