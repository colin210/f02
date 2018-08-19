from flask import render_template,redirect,request,url_for,flash
from . import leader
# from .models import Leader
from .forms import LeaderForm
from app import db


@leader.route('/', methods=['GET'])
def index():
    from .models import Leader
    leader1 =Leader(group_name='1', name='1', age='1', city='sh')
    leader1=leader1
    return 'ok'