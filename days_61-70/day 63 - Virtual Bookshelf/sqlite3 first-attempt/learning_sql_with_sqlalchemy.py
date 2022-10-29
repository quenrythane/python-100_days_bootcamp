from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()  # need to add the context to code work properly
# (don't know why yet but this line make db.create_all() and db.session.commit() works)
# look into this thread 👉 https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask
"""
When creating your app, use:
    app.app_context().push()
for example like this:
    from your_app import create_app
    app = create_app()
    app.app_context().push()
for further information: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
"""


# CREATE an SQLite DATABASE called new-books-collection.db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"  # this create instance folder
# and new-books-collection.db file inside
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE a TABLE in this database called book (after the class name - but with lowercase).
# define columns and properties
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)  # nullable=False means can't be empty field
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# DROP previous data
db.drop_all()  # 3:)

# CREATE a TABLE define above
db.create_all()
# Sometimes To create the initial database run:
"""
with app.app_context():
    db.create_all()
"""


# CREATE a new entry in the books table
# it's HAVE TO be **kwargs (the documentation says it)
new_book = Book(id=1,
                title="Harry Potter",
                author="J. K. Rowling",
                rating=9.3)
# NOTE: When creating new records, the primary key fields is optional. you can also write without this **kwargs:
# adding record to database
db.session.add(new_book)
db.session.commit()  # this line throws an error


# READ
# all records
all_books = db.session.query(Book).all()
all_books_2 = Book.query.all()
print(all_books)
print(all_books_2)

# a particular record by query
book = Book.query.filter_by(title="Harry Potter").first()


# UPDATE
# A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()


# DELETE
# A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


# Flask app start here
if __name__ == "__main__":
    app.run(debug=True, port=63, use_reloader=False)
