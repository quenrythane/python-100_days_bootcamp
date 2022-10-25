from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []


class BookForm(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = SelectField("Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    message = False
    if request.method == "POST":
        message = True
        all_books.append({
            "title": form.title.data,
            "author": form.author.data,
            "rating": form.rating.data
        })
        print(all_books[-2:])

        book_name = form["title"].data
        return render_template("add.html", form=form, message=message, book_name=book_name)
    print(form.validate_on_submit(), form.data)
    return render_template("add.html", form=form, message=message)


if __name__ == "__main__":
    app.run(debug=True, port=63)

