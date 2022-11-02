from flask import Flask, render_template  # , request, redirect, url_for
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()  # need to add the context to code work properly
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my-library-books-collection.db"  # this create instance folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class MyLibraryBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)  # nullable=False means can't be empty field
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(5), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# CREATE a TABLE define above
db.create_all()


class BookForm(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = SelectField("Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
    submit = SubmitField('Add Book')


@app.route('/')
def home():
    all_books = MyLibraryBooks.query.all()
    print(all_books)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    message = False
    if form.validate_on_submit():
        message = True
        # prepare new entry
        new_book = MyLibraryBooks(title=form.title.data,
                                  author=form.author.data,
                                  rating=form.rating.data)
        # add and commit new entry
        db.session.add(new_book)
        db.session.commit()  # this line throws an error

        all_books = MyLibraryBooks.query.all()
        return render_template("index.html", all_books=all_books)
    return render_template("add.html", form=form, message=message)


if __name__ == "__main__":
    app.run(debug=True, port=63)
