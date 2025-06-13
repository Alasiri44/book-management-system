# 📚 Book Review Platform

A Flask-based web application that allows users to manage books, authors, and reviews. It includes full CRUD operations, relational modeling with SQLAlchemy, database migrations, and optional web scraping to seed the database with book data.

## Setup

We'll build up our Flask application from a few models and views that are ready
to go. Run these commands to install the dependencies and set up the database:

```console
$ pipenv install; pipenv shell
$ cd server
$ flask db init
$ flask db migrate -m 'initial migration'
$ flask db upgrade head
$ python seed.py
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

You can view the models in the `server/models.py` module, and the migrations in
the `server/migrations/versions` directory. 

Then, run the server:

```console
$ python app.py
```

With that set up, let's work on getting Flask and SQLAlchemy working together!

---

## 🛠 Tech Stack

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- Flask-Migrate  
- BeautifulSoup4 (optional scraping)  
- Requests  

---

## 📂 Project Structure
book-review-platform/
├── app.py
├── models.py
├── seed.py
├── scrape_books.py (optional)
├── requirements.txt
├── migrations/
└── templates/ (if applicable)


---

## 🚀 Features

### 1. **Modeling Relationships**
- **Author**:  
  - `name`  
  - One-to-many with `Book`  

- **Book**:  
  - `title`, `publication_year`  
  - Many-to-many with `Review` via an association table  

- **Review**:  
  - `rating` (1–5), `comment`  
  - Belongs to a `Book`  

Relationships are managed using `db.relationship()` and `backref`.

---

### 2. **Database Migrations & Seeding**
- Flask-Migrate is used for schema migrations.  
- Run `flask db init`, `flask db migrate`, and `flask db upgrade` to manage schema.  
- `seed.py` populates the database with:
  - 2 Authors
  - 4 Books
  - 6 Reviews

---

### 3. **API Endpoints**

#### ✅ `GET /books`
Returns a JSON list of all books including:
- Title
- Publication year
- Author name
- Associated reviews (with rating & comment)

#### ✅ `GET /books/<id>`
Returns one book by ID with full details.

#### ✅ `POST /books`
Adds a new book via JSON payload:
```json
{
  "title": "Sample Title",
  "publication_year": 2021,
  "author_id": 1
}

