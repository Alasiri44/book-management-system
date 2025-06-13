from faker import Faker
from app import app
from models import Book, Review, Author, db

fake = Faker()

with app.app_context():
    Book.query.delete()
    Author.query.delete()
    Review.query.delete()
    
    authors = []
    for i in range(20):
        author = Author(name=fake.name())
        authors.append(author)
    db.session.add_all(authors)
    db.session.commit()