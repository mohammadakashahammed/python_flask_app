from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1> hello, world!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize))


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/users/<int:user_id>')
def greet_user(user_id):
    users = ['Anan', 'Numan', 'Shuvo', 'Sifat']
    try:
        return '<h2>hi {}</h2>'.format(users[user_id])
    except IndexError:
        about(404)


if __name__ == "__main__":
    app.run(debug=True)
