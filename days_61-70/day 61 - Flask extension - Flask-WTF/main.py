from flask import Flask, render_template, request
from wtforms import Form, PasswordField, StringField, validators, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template('index.html')


# wtforms
class LoginForm(FlaskForm):
    email = StringField('Email:', [validators.Email()])
    password = PasswordField(label='Password:', validators=[validators.Length(min=8, message="wrong length")])
    submit = SubmitField("Log In")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # if request.method == 'POST':  # and login_form.validate():
    if login_form.validate_on_submit():
        print("1 email data:", login_form.email.data)
        print("2 password data:", login_form.password.data)
        print("3 validate:", login_form.validate())
        if "artur" in login_form.email.data.lower():
            return render_template("success.html")
        else:
            return render_template("denied.html")

    login_form.validate()
    return render_template('login.html', form=login_form)


@app.route("/denied", methods=["GET", "POST"])
def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True, port=61)
