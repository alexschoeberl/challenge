from catalogue import database as db


class Book(db.Model):
    __tablename__ = 'Books'

    idf = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    editor = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)

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
