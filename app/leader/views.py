from flask import render_template,redirect,request,url_for,flash
from . import leader
from .models import Leader
from .forms import LeaderForm
from app import db


@leader.route('/', methods=['GET', 'POST'])
def index():
    form = LeaderForm()
    if form.validate_on_submit():
        leader_info = Leader(group_name=form.group_name.data,
                            age=form.age.data,
                            name=form.name.data)
        db.session.add(leader_info)
    leader_all = Leader.query.all()

    return render_template('leader/index.html', leader_all=leader_all, form=form)


@leader.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    leader_edit = Leader.query.get(id)
    form = LeaderForm(group_name=leader_edit.group_name,
                         name=leader_edit.name,
                         age=leader_edit.age)

    if leader_edit:
        try:
            if form.validate_on_submit():
                leader_edit.group_name = form.group_name.data,
                leader_edit.age = form.age.data,
                leader_edit.name = form.name.data,
                db.session.add(leader_edit)
                db.session.commit()
                return redirect(url_for('leader.index'))
        except Exception as e:
            print(e)
            db.session.rollback()
    return render_template('leader/edit.html', form=form)



@leader.route('/delleader/<id>', methods=['GET','POST'])
def delleader(id):
    leader_del = Leader.query.get(id)
    if leader_del:
        try:
            db.session.delete(leader_del)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    return redirect(url_for('leader.index'))