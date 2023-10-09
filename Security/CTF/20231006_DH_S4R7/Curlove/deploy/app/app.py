from flask import Flask, request, render_template, session, redirect, abort
from query import get_user, register_user
from hashlib import sha256
from re import search
from os import urandom
import subprocess


app = Flask(__name__)
app.secret_key = urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "DH{{This_is_flag}}"


@app.route("/", methods=["GET"])
def index():
    if not session:
        return render_template("login.html")
    
    elif session["isAdmin"] == True:
        return render_template("admin.html")
    
    else:
        return render_template("guest.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "" or password == "":
            return render_template("login.html", msg="Enter username and password")

        sha256_password = sha256((password).encode()).hexdigest()
        try:
            user = get_user(username, sha256_password)

            if user:
                if user[1].startswith("admin"):
                    session["username"] = user[1]
                    session["isAdmin"] = True
                    session["login"] = True
                    return redirect("/admin")
                else:
                    session["username"] = user[1]
                    session["isAdmin"] = False
                    session["login"] = True
                    return redirect("/guest")
            else:
                return render_template("login.html", msg="Login Failed..."), 401
        except Exception as e:
            abort(500)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "" or password == "":
            return render_template("login.html", msg="Enter username and password")

        m = search(r".*", username)

        if username or m:
            if m.group().strip().find("admin") == 0:
                return render_template("signup.html", msg="Not allowed username"), 403
            else:
                username = username.strip()
                sha256_password = sha256((password).encode()).hexdigest()
                register_user(username, sha256_password)
                return redirect("/login")


@app.route("/guest", methods=["GET"])
def guest():
    if not session:
        return redirect("/login")

    return render_template("guest.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session:
        return redirect("/login")
    
    if session["isAdmin"] == False:
        return redirect("/guest")

    if request.method == "GET":
        return render_template("admin.html")

    if request.method == "POST":
        url = request.form["url"].strip()

        if (url[0:4] != "http") or (url[7:20] != "dreamhack.io/"):
            return render_template("admin.html", msg="Not allowed URL")

        if (".." in url) or ("%" in url):
            return render_template("admin.html", msg="Not allowed path traversal")
        
        if url.endswith("flag") or ("," in url):
            return render_template("admin.html", msg="Not allowed string or character")
        try:
            response = subprocess.run(
                ["curl", f"{url}"], capture_output=True, text=True, timeout=1
            )
            return render_template("admin.html", response=response.stdout)

        except subprocess.TimeoutExpired:
            return render_template("admin.html", msg="Timeout !!!")


@app.route("/flag", methods=["GET"])
def flag():
    ip_address = request.remote_addr
    if ip_address == "127.0.0.1":
        return FLAG
    else:
        return "Only local access allowed", 403


app.run(host="0.0.0.0", port=80)
