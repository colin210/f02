from flask import render_template,redirect,request,url_for,flash
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,login_required,logout_user
from app import db



@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user is not None or user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            print('hhah')
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('invalid username')
    print('sss')
    return render_template('auth/login.html',form=form)


@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        print(user)
        db.session.add(user)
        # db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)

@auth.route('/login1')
def login1():
    return 'auth hello login1111'


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logout')
    return redirect(url_for('main.index'))