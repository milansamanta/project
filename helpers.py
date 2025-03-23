from functools import wraps
from flask import session, redirect, render_template
import requests

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return redirect('/login')
        return f(*args, **kwargs)
    return wrapper

def escape(s):
    for old, new in [
        ('-', '--'),
        (' ', '-'),
        ('_', '__'),
        ("?", "~q"),
        ("%", "~p"),
        ("#", "~h"),
        ("/", "~s"),
        ('"', "''"),
    ]:
        s = s.replace(old, new)
    return s

def apology(messege):        
    return render_template("apology.html", messege=escape(messege))

def lookup(s):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{escape(s)}")
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    return response.json()
