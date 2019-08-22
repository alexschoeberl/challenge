from catalogue import database as db


class Book(db.Model):
    __tablename__ = 'Books'

    idf = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'idf': self.idf,
            'title': self.title,
            'author': self.author
        }
    
    def update(self, title=None, author=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author

    def __repr__(self):
        return f'<Book {self.idf}>'
