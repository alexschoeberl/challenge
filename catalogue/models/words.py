from datetime import datetime

from catalogue import database as db


class Word(db.Model):
    __tablename__ = 'Words'

    key = db.Column(db.String, primary_key=True)
    book_idf = db.Column(db.Integer, db.ForeignKey('Books.idf'), nullable=False)
    book = db.relationship('Book', backref=db.backref('words', cascade='all, delete-orphan'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def serialize(self):
        return {
            'word': self.key,
            'book': self.book,
            'created_at': self.created_at.strftime('%Y.%m.%d %H:%M:%S')
        }

    def __repr__(self):
        return f'<Word {self.word}>'
