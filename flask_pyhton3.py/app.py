
from flask import Flask,jsonify
from markupsafe import escape
from flask import Flask, abort

# ...

app = Flask(__name__)

# ...


@app.route('/')
@app.route('/index/')
def hello():
     return jsonify("Hello, World!")


@app.route('/about/')
def about():
    return jsonify("This is a Flask web application")


@app.route('/capitalize/<word>/')
def capitalize(word):
    return jsonify(escape(word.capitalize()))

# ...

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return jsonify(format(n1 + n2))



@app.route('/sub/<int:n1>/<int:n2>/')
def sub(n1, n2):
    return jsonify(format(n1 - n2))


# ...
@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return jsonify(format(users[user_id]))
    except IndexError:
        abort(404)
