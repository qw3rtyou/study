import sqlite3
import os
import uuid
import hashlib
from flask import Flask, flash,request, session,render_template, make_response, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = os.urandom(32)

DATABASE = 'database.db'

FLAG = "FLAG{test_flag}"

def init_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            user_ID TEXT NOT NULL,
            user_PW TEXT NOT NULL,
            money INTEGER NOT NULL DEFAULT 500,
            user_cheeese INTEGER DEFAULT 0,
            user_flag INTEGER DEFAULT 0,
            unique(user_ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            content TEXT NOT NULL,
            unique(name)
        )
    ''')

    cursor.execute("INSERT OR IGNORE INTO items (name, price, content) VALUES (?, ?, ?)", ('cheeeese', 500, 'hehe'))
    cursor.execute("INSERT OR IGNORE INTO items (name, price, content) VALUES (?, ?, ?)", ('FLAG', 5000, FLAG))
    db.commit()

def execute_query(query, values=None):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    if values is None:
        cursor.execute(query)
    else:
        cursor.execute(query, values)
    conn.commit()
    return cursor


def get_user(user_id):
    user = execute_query('SELECT * FROM user WHERE user_ID = ?', (user_id,)).fetchone()
    if user:
        return user
    return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    return render_template('market.html')

@app.route('/refund')
def refund():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    return render_template('refund.html')

@app.route('/mypage')
def mypage():
    
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    flag = user[5]
    if user[5] > 0:
        flag = execute_query("SELECT * FROM items where name='FLAG'").fetchone()[3]
    return render_template("mypage.html",money=user[3],cheese=user[4],flag=flag)
    



@app.route("/item/refund/cheeese",methods=['GET'])
def cheese_refund():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    cheese_num = user[4]
    
    
    if cheese_num <= 0:
        return "<script>alert('you Don have cheese!');location.href='/'</script>"


    cheese_num -= 1
    
    execute_query('UPDATE user SET money=money+500, user_cheeese=? where user_ID=?',(cheese_num,session['id']))
    return "<script>alert('Thank you!');location.href='/'</script>"
    

@app.route('/item/purchase/flag', methods=['GET'])
def flag_purchase():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    flag_num = user[5]
   
    
    if user_money < 5000:
        return "<script>alert('Not enough money!');location.href='/'</script>"
    
    
    user_money -= 5000
    flag_num += 1
    
    execute_query('UPDATE user SET money=?, user_flag=? where user_ID=?',(user_money,flag_num,session['id']))
    
    return "<script>alert('Thank you!');location.href='/'</script>"
        
@app.route('/item/purchase/cheeese', methods=['GET'])
def cheese_purchase():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    cheese_num = user[4]
    

    if user_money < 100:
        return "<script>alert('Not enough money!');location.href='/'</script>"
    
    cheese_num += 1
    
    execute_query('UPDATE user SET money=money-500, user_cheeese=? where user_ID=?',(cheese_num,session['id']))
    
    return "<script>alert('Thank you!');location.href='/'</script>"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    
    user_id = request.form['id']
    user_pw = request.form['pw']
    user_pw = hashlib.sha256(user_pw.encode()).hexdigest()
    
    user = execute_query("SELECT * FROM user where user_ID=? AND user_PW=?", (user_id, user_pw)).fetchone()

    
    if user == None:
        return "<script>alert('fail!');location.href='/login'</script>"
        
    session['id'] = user[1]
    print(user)
    return redirect('/')

    
@app.route('/register', methods=['POST',"GET"])
def register():
    if request.method=='GET':
        return render_template('regist.html')

    user_id = request.form['id']
    user_pw = request.form['pw']
    
    if get_user(user_id) != None:
        return render_template('index.html')
    
    user_pw = hashlib.sha256(user_pw.encode()).hexdigest()
    execute_query('INSERT INTO user (user_ID, user_PW) VALUES (?, ?)', (user_id, user_pw))

    return "<script>alert('Success!');location.href='/login'</script>"
    
        

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=10011, threaded=True)

