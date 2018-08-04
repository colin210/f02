from flask import render_template,redirect,request,url_for,flash
from . import info
from ..models import Qa
from .forms import QaForm
from app import db


@info.route('/index',methods=['GET','POST'])
def index():
    form = QaForm()
    if form.validate_on_submit():
        qa = Qa(name=form.name.data,
                    age=form.age.data)
        db.session.add(qa)
    qa_all = Qa.query.all()
    print(qa_all)
    return render_template('info/index.html',qa_all=qa_all, form=form)




@info.route('/add',methods=['GET','POST'])
def add():
    form = QaForm()
    if form.validate_on_submit():
        qa = Qa(name=form.name.data,
                    age=form.age.data)
        db.session.add(qa)
        return redirect(url_for('info.add'))
    return render_template('info/add.html',form=form)


@info.route('/delqa/<id>',methods=['GET','POST'])
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

