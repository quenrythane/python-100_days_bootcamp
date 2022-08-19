from flask import Flask
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return 'Hello Succeeded!'


@app.route('/bye')
def bye_world():
    return 'Bye Succeeded!'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name.capitalize()}!'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="" , port=5000)
