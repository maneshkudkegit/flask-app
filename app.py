from flask import Flask
from markupsafe import escape

# ...

app = Flask(__name__)

# ...


@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

# ...

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/sub/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 - n2)