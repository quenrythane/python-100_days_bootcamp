from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    # return render_template('main_page/index.html')
    return render_template('index.html')  # templates: https://html5up.net/


if __name__ == '__main__':
    app.run(debug=True, port=56)
