# coding: utf-8
from flask import Flask, render_template, request,send_from_directory
from flask_bootstrap  import  Bootstrap
from nameForm import NameForm
import time, os

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'colin'
bootstrap = Bootstrap(app)


@app.route('/',  methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


@app.route('/upload', methods=['POST'])
def upload():
    fname = request.files.get('file')
    if fname :
        t = time.strftime('%Y%m%d%H%M%S')
        new_fname = r'upload/' + fname.filename + t
        fname.save(new_fname)
        return '{"code": "ok"}'
    else:
        return '{"msg": "请上传文件！"}'


@app.route('/getfiles', methods=['GET'])
def getfiles():
    fpath = request.values.get('fpath', '')
    print(fpath)
    if os.path.isdir(fpath):
        filelist = os.listdir(fpath)
        files = [file for file in filelist if os.path.isfile(os.path.join(fpath, file))]
    return str(files)


@app.route('/download', methods=['get'])
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


if __name__ == '__main__':
    app.run()
