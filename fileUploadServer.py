# coding: utf-8

import requests
import os


def uploadfiletoserver():
    file = {'file': open('Requirements', 'rb')}
    r = requests.post('http://127.0.0.1:5000/upload', files=file)
    print(r.text)
    return r.text


def getfilename():
    r1 = requests.get('http://127.0.0.1:5000/getfiles', data={'fpath': r'upload/'})
    print(r1.text)
    return r1.text


def downloadfile():
    a =getfilename()[2:-2]
    r2 = requests.get('http://127.0.0.1:5000/download',data={'filename': a, 'path': r'upload/'})
    file = r2.text #获取文件内容
    basepath = os.path.join(os.path.dirname(__file__), r'download/')
    with open(os.path.join(basepath, 'hello_download.txt'),'a',encoding='utf-8') as f: #保存文件
        f.write(file)

