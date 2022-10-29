from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create an SQLite database called new-books-collection.db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create a table in this database called books.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)  # nullable=False means can't be empty field
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# To create the initial database run:
db.create_all()


# Create a new entry in the books table
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)  # it's HAVE TO be **kwargs (the documentation says it)
# adding record to database
db.session.add(new_book)
db.session.commit()


# Flask app start here
if __name__ == "__main__":
    app.run(debug=True, port=63, use_reloader=False)
