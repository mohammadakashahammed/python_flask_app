from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1> hello, world!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


if __name__ == "__main__":
    app.run(debug=True)
