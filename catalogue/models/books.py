from catalogue import database as db


class Book(db.Model):
    """Database model for the books table"""
    __tablename__ = 'Books'

    idf = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=True)
    editor = db.Column(db.String, nullable=True)
    publisher = db.Column(db.String, nullable=True)
    language = db.Column(db.String, nullable=True)

    def serialize(self):
        return {
            'idf': self.idf,
            'title': self.title,
            'author': self.author,
            'editor': self.editor,
            'publisher': self.publisher,
            'language': self.language
        }

    def __repr__(self):
        return f'<Book {self.idf}>'
