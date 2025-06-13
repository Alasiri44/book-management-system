from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Association table to store many to many relationship between books and reviews
book_reviews = db.Table(
    'books_reviews',
    metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('review_id', db.Integer, db.ForeignKey('reviews.id'), primary_key=True)
)

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'
    
    serialize_only = ('title', 'publication_year', 'author.name', 'reviews')
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
    # Relationship showing which author has written a book
    author = db.relationship('Author', back_populates='books')
    
    reviews = db.relationship('Review', secondary=book_reviews, back_populates='books')
    
    def __repr__(self):
        return f'<Book {self.id}, {self.title}, {self.publication_year}>'

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    # Relationship referencing the author to books
    books = db.relationship('Book', back_populates='author')
    
    serialize_only = ('name', )
    
    def __repr__(self):
        return f'<Author {self.id}, {self.name}>'

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    links = db.Column(db.String)
    
    books = db.relationship('Book', secondary=book_reviews, back_populates='reviews')
    
    serialize_only = ('rating', 'comment', 'links' )
    def __repr__(self):
        return f'<Review {self.id}, {self.rating}, {self.comment}>'