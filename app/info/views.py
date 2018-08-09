from flask import render_template,redirect,request,url_for,flash
from . import info
from ..models import Qa
from .forms import QaForm,QaFormEdit
from app import db
from ..phone.models import Phone


@info.route('/index', methods=['GET', 'POST'])
def index():
    form = QaForm()
    if form.validate_on_submit():
        qa = Qa(name=form.name.data,
                age=form.age.data)
        db.session.add(qa)
    qa_all = Qa.query.all()

    # count = []
    # for i in qa_all:
    #     count.append(Phone.query.filter_by(qa_id=i.id).count())
    return render_template('info/index.html', qa_all=qa_all, form=form)


@info.route('/add', methods=['GET', 'POST'])
def add():
    form = QaForm()
    if form.validate_on_submit():
        qa = Qa(name=form.name.data,
                    age=form.age.data)
        db.session.add(qa)
        return redirect(url_for('info.add'))
    return render_template('info/add.html', form=form)


@info.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    qa_edit = Qa.query.get(id)
    form = QaFormEdit(name=qa_edit.name, age=qa_edit.age)
    if qa_edit:
        try:
            if form.validate_on_submit():
                qa_edit.name = form.name.data,
                qa_edit.age = form.age.data,
                db.session.add(qa_edit)
                db.session.commit()
                return redirect(url_for('info.index'))
        except Exception as e:
            print(e)
            db.session.rollback()
    return render_template('info/edit.html',form=form)


@info.route('/delqa/<id>', methods=['GET', 'POST'])
def delqa(id):
    qa_del = Qa.query.get(id)
    if qa_del:
        try:
            db.session.delete(qa_del)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    return redirect(url_for('info.index'))


@info.route('/phone/<id>', methods=['GET', 'POSt'])
def phone(id):
    phone_all = Phone.query.filter_by(qa_id=id)
    return render_template('info/phone.html', phone_all=phone_all)
