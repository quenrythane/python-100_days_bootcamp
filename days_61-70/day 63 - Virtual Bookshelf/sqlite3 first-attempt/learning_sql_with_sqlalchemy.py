from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "new-books-collection.db"
db = SQLAlchemy(app)

# db = sqlite3.connect("books-collection.db")
# db = "new-books-collection.db"
