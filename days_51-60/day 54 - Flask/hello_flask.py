from flask import Flask
from my_flask_decorators import *
from random import randint
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return 'Hello Succeeded!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return 'Bye Succeeded!'


@app.route('/hello/<name>')  # <name> means a variable
def hello_name(name):
    return f'Hello {name.capitalize()}!'


"""
@app.route('/hello/<path:name>')  # read variable as a path
@app.route('/hello/<int:name>')  # read variable as a integer
def hello_name(name):
    return f'Hello {name.capitalize()}!'
"""


# decorator exercise
@app.route("/woman/<woman>")
@is_woman
def woman(woman):
    return woman


# final guess a number project
@app.route("/higher-lower")
def higher_lower_root():
    return "Guess a number between 0 and 9"


@app.route("/higher-lower/<number>")
def higher_lower_guess():
    return "Guess a number between 0 and 9"




if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="" , port=5000)
