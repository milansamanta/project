from flask import Flask, request, render_template, redirect, session, jsonify
from flask_session import Session
from sqlite3 import connect, Row
from helpers import login_required, apology, lookup
from werkzeug.security import generate_password_hash, check_password_hash
import requests


app = Flask(__name__)

app.jinja_env.filters["lookup"] = lookup
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
@login_required
def ok():
    return redirect("/0")

@app.route("/<int:factor>")
@login_required
def index(factor=0):
    offset = factor * 20
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=20")
        response.raise_for_status()  
        data = response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching data: {e}", 500
    return render_template("index.html", data=data, factor=factor)

@app.route("/pokemon")
@login_required
def red():
    return redirect("/pokemon/1")

@app.route("/pokemon/<int:id>")
@login_required
def pokemon(id):
    data = lookup(str(id))
    if not data:
        return apology("no pokemon data")
    others = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
    
    return render_template("pokemon.html", data=data)

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology('must provide username')
        if not request.form.get('password'):
            return apology('must provide password')
        cx = connect("users.db")
        cx.row_factory = Row
        cu = cx.cursor()
        rows = [dict(r) for r in cu.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"), )) ]
        if not rows:
            return apology("username don't exist")
        row = rows[0]
        if not check_password_hash(row['hash'], request.form['password']):
            return apology("wrong password")
        session['user_id'] = row['id']
        return redirect("/0")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")
        if not request.form.get('password'):
            return apology("must provide password")
        if request.form.get('confirmation', None) != request.form.get("password"):
            return apology("password don't match")
        cx = connect("users.db")
        cx.row_factory = Row
        cu = cx.cursor()
        try:
            cu.execute("INSERT INTO users(username, hash) VALUES(?, ?)", (request.form.get("username"), generate_password_hash(request.form.get("password")) ))
            cx.commit()
            cx.close()
        except:
            cx.close()
            return apology("username already exists")
        return redirect("/login")
    return render_template("register.html")


@app.route("/search")
@login_required
def search():
    pokemon = request.args.get("q")
    if not pokemon:
        return apology("searched nothing")
    cx = connect("pokedata.db")
    cx.row_factory = Row
    cu = cx.cursor()
    data = [ dict(row) for row in cu.execute("SELECT * FROM pokedata WHERE name LIKE ?", (pokemon+"%", )) ]
    return render_template("search.html", data = data)

@app.route("/searched")
def searched():
    pokemon = request.args.get("q")
    if pokemon:
        cx = connect("pokedata.db")
        cx.row_factory = Row
        cu = cx.cursor()
        data = [ dict(row) for row in cu.execute("SELECT * FROM pokedata WHERE name LIKE ? ", (pokemon+"%", )) ]
    else:
        data = []
    return jsonify(data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")