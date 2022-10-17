from flask import Flask, render_template
from wtforms import Form, PasswordField, StringField, validators

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


# wtforms
class RegistrationForm(Form):
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Password:', [validators.Length(min=4, max=25)])


@app.route("/login")
def login():
    login_form = RegistrationForm()
    return render_template('login.html', form=login_form)




if __name__ == '__main__':
    app.run(debug=True, port=61)
