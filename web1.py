from flask import Flask
from flask import render_template
from flask import request
import demo
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

import os 
from flask import send_from_directory     

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='imag/av2.png')

import cx_Oracle

@app.route('/login', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def signin():
    
    username = request.form['username']
    password = request.form['password']

    
    if password=='123':
        return render_template('index.html', message='OK',username=username)
    else:
        return render_template('password.html', message='Bad username or password', username=username)
    return render_template('password.html',  username=username)


def getdb(id):
        dsn=cx_Oracle.makedsn("192.168.242.155",1521,'orcl')
        conn=cx_Oracle.connect("c##beijing","123456",dsn)
        curs=conn.cursor()
        user=id
        sql="select pwd from t_login where name='"+user+"'"
        curs.execute(sql)
        dataset=curs.fetchone()
        print(dataset[0])
        return dataset[0]

@app.route('/head', methods=['GET'])
def head():
    
    return render_template('head.html')
@app.route('/left', methods=['GET'])
def left():
    
    return render_template('left.html')
@app.route('/grade', methods=['GET'])
def grade():
    
    return render_template('demo.html')
@app.route('/information')
def list_connection_show():
    nodeinfo = demo.list_connection()
    return render_template('connection_show.html',information=nodeinfo)

@app.route('/show')
def machine():
    a=demo.show_machine()
    return render_template('show.html',open=a[0],close=a[1])


@app.route('/close')
def close_connection():
    num=demo.close_connection()
    return render_template('close.html',think=num)
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create',methods=['POST'])
def create_():
    name = request.form['name']
    isok=demo.create(name)
    return render_template('create.html',isok=isok)
@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/start', methods=['POST'])
def start_():
    name = request.form['name']
    isok = demo.start(name)
    return render_template('start.html', isok=isok)

@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')


@app.route('/shutdown', methods=['POST'])
def shutdown_():
    name = request.form['name']
    isok = demo.shutdown(name)
    return render_template('shutdown.html', isok=isok)



@app.route('/del')
def del_():
    return render_template('del.html')


@app.route('/del', methods=['POST'])
def del__():
    name = request.form['name']
    isok = demo.destroy(name)
    return render_template('del.html', isok=isok)
if __name__ == '__main__':
    app.run(host='192.168.242.155',port=5000)
    #app.run()
    
