from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Book, Author, Review
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to the Book Review Platform</h1>'

@app.route('/books')
def books():
    books = Book.query.all()
    response_body = []
    for book in books:
        body = book.to_dict()
        response_body.append(body)
    return make_response(response_body, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)