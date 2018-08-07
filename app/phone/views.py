from flask import render_template,redirect,request,url_for,flash
from . import phone
from .models import Phone
from .forms import PhoneForm, SelectPhoneForm,PhoneFormEdit
from app import db


@phone.route('/index',methods=['GET','POST'])
def index():
    form = PhoneForm()
    if form.validate_on_submit() :
        phone = Phone(machine_os=form.machine_os.data,
                      machine_year=form.machine_year.data,
                      machine_pinpai= form.machine_pinpai.data)
        db.session.add(phone)
    phone_all = Phone.query.all()
    return render_template('phone/index.html',phone_all=phone_all, form=form)



@phone.route('/check',methods=['GET','POST'])
def check():
    form = SelectPhoneForm()
    if form.validate_on_submit() :
        machine_os = form.machine_os.data,
        machine_pinpai = form.machine_pinpai.data
        phone_all = Phone.query.filter_by(machine_os=machine_os,machine_pinpai = machine_pinpai).all()

        return render_template('phone/check.html', phone_all=phone_all, form = form)
    return render_template('phone/check.html', form=form)



@phone.route('/add',methods=['GET','POST'])
def add():
    form = PhoneForm()
    if form.validate_on_submit():
        phone = Phone(machine_os=form.machine_os.data,
                      machine_year=form.machine_year.data,
                      machine_pinpai=form.machine_pinpai.data)
        db.session.add(phone)
        return redirect(url_for('phone.add'))
    return render_template('phone/add.html',form=form)


@phone.route('/delphone/<id>',methods=['GET','POST'])
def delphone(id):
    phone_del = Phone.query.get(id)
    if phone_del:
        try:
            db.session.delete(phone_del)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    return redirect(url_for('phone.index'))


@phone.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    phone_edit = Phone.query.get(id)
    form = PhoneFormEdit(machine_os = phone_edit.machine_os,machine_year = phone_edit.machine_year,machine_pinpai = phone_edit.machine_pinpai)
    if phone_edit:
        try:
            if form.validate_on_submit():
                phone_edit.machine_os = form.machine_os.data
                phone_edit.machine_year = form.machine_year.data
                phone_edit.machine_pinpai = form.machine_pinpai.data
                db.session.add(phone_edit)
                db.session.commit()
                return redirect(url_for('phone.index'))
        except Exception as e:
            print(e)
            db.session.rollback()
    return render_template('phone/edit.html',form=form)



