from flask import Flask, session, render_template, request
import os, time

app = Flask(__name__)
app.secret_key = os.urandom(30)
FLAG = 'A'
PORT = 80

@app.route('/', methods = ['GET'])
def home():
    if not 'cash' in session:
        session['cash'] = 10000
    try:
        session['cash'] -= int(request.args['cash'])
    except:
        pass
    
    flag = ''
    if session['cash'] > 100000000:
        print('[FLAG]', time.ctime(time.time()), request.remote_addr)
        flag = FLAG
    return render_template('index.html', cash = session['cash'], flag = flag)
    
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT)
