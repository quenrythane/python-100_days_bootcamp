from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello Succeeded!'

@app.route('/bye')
def bye_world():
    return 'Bye Succeeded!'

if __name__ == '__main__':
    app.run()

