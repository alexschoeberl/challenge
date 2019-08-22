from catalogue import database as db


class Preference(db.Model):
    """Database model for the preferences table"""
    __tablename__ = 'Preferences'

    book_idf = db.Column(db.Integer, db.ForeignKey('Books.idf'), primary_key=True)
    book = db.relationship('Book', backref=db.backref('preferences', cascade='all, delete-orphan'), uselist=False)
    char_min = db.Column(db.Integer, default=0, nullable=False)
    char_max = db.Column(db.Integer)

    def serialize(self):
        return {
            'book': self.book,
            'char_min': self.char_min,
            'char_max': self.char_max
        }

    def __repr__(self):
        return f'<Preference {self.book.idf}>'
