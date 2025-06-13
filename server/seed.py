from faker import Faker
from app import app
from models import Book, Review, Author, db, book_reviews
from random import choice, randint

fake = Faker()

with app.app_context():
    db.session.query(book_reviews).delete()
    Book.query.delete()
    Author.query.delete()
    Review.query.delete()
    
    authors = []
    for i in range(20):
        author = Author(name=fake.name())
        authors.append(author)
    db.session.add_all(authors)
    
    books = []
    for i in range(50):
        book= Book(title=fake.sentence(nb_words=4).rstrip('.'),publication_year=fake.date_between(start_date='-70y', end_date='-18y'), author=choice(authors))
        books.append(book)
    db.session.add_all(books)
   
    
    reviews = []
    for i in range(100):
        review = Review(
        rating=randint(1, 5),
        comment=fake.paragraph(nb_sentences=2),
        links=f'https://www.book/{(choice(books)).title}'     
    )
        reviews.append(review)
    # Link the review to 1–3 random books
    review.books = [choice(books) for _ in range(randint(1, 40))]
    db.session.add_all(reviews)
    db.session.commit()