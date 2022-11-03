from flask import Flask, render_template, request, redirect, url_for
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
    submit2 = SubmitField('Edit Rating')



@app.route('/')
def home():
    all_books = MyLibraryBooks.query.all()
    print(all_books)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # prepare new entry
        new_book = MyLibraryBooks(  # id is autogenerate and auto increase
                                title=form.title.data,
                                author=form.author.data,
                                rating=form.rating.data)
        # add and commit new entry
        db.session.add(new_book)
        db.session.commit()  # this line throws an error

        all_books = MyLibraryBooks.query.all()
        return render_template("index.html", all_books=all_books)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = BookForm()
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]  # bo in edit_rating.html <input hidden="hidden" name="id" value="{{book.id}}">
        print(book_id, 'xd')
        book_to_update = MyLibraryBooks.query.get(book_id)
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('book_id')
    print(book_id, 'xdd')  # bo in index.html <a href="{{ url_for('edit', book_id=book.id) }}">Edit Rating</a>
    book_selected = MyLibraryBooks.query.get(book_id)
    return render_template("edit_rating.html", form=form, book=book_selected)

"""
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
"""



@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = MyLibraryBooks.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=63)
