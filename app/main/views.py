# coding: utf-8
from flask import Flask, render_template, request,send_from_directory
import time
import os
from . import main
from .forms import NameForm
from .. import db
from ..models import User



@main.route('/',  methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)
    # return render_template('user.html', form=form, name=name)


@main.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


@main.route('/upload', methods=['POST'])
def upload():
    fname = request.files.get('file')
    if fname :
        t = time.strftime('%Y%m%d%H%M%S')
        new_fname = r'upload/' + fname.filename + t
        fname.save(new_fname)
        return '{"code": "ok"}'
    else:
        return '{"msg": "请上传文件！"}'


@main.route('/getfiles', methods=['GET'])
def getfiles():
    fpath = request.values.get('fpath', '')
    print(fpath)
    if os.path.isdir(fpath):
        filelist = os.listdir(fpath)
        files = [file for file in filelist if os.path.isfile(os.path.join(fpath, file))]
    return str(files)


@main.route('/download', methods=['get'])
def download():
    fpath = request.values.get('path', '') #获取文件路径
    fname = request.values.get('filename', '')  #获取文件名
    if fname.strip() and fpath.strip():
        print(fname, fpath)
        if os.path.isfile(os.path.join(fpath,fname)) and os.path.isdir(fpath):
            return send_from_directory(fpath, fname, as_attachment=True) #返回要下载的文件内容给客户端
        else:
            return '{"msg":"参数不正确"}'
    else:
        return '{"msg":"请输入参数"}'

