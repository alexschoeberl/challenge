from flask import request
from flask_restful import abort, reqparse, Resource

from catalogue import database as db
from catalogue.models.books import Book as BookModel
from catalogue.models.preferences import Preference as PreferenceModel
from catalogue.models.words import Word as WordModel
from catalogue.abstract import analyse_abstract, parse_abstract


class WordList(Resource):
    def get(self, idf):
        book = BookModel.query.get_or_404(idf)
        words = WordModel.query.filter_by(book_idf=book.idf).all()
        words = [serialize(word) for word in words]
        return words, 200

    def post(self, idf):
        book = BookModel.query.get_or_404(idf)
        pref = PreferenceModel.query.get_or_404(book.idf)
        body = Word.parse_reqest()

        keys = parse_abstract(body['abstract'], pref.char_min, pref.char_max)
        for key in keys:
            word = WordModel.query.get(key)
            if word is None:
                word = WordModel(key=key, book_idf=book.idf)
                db.session.add(word)
        db.session.commit()

        most, least = analyse_abstract(body['abstract'], pref.char_min, pref.char_max)

        return {
            'url': locate_vocabulary(book),
            'most_common': most,
            'least_common': least
        }, 201


class Word(Resource):
    parser = None

    def get(self, idf, key):
        word = WordModel.query.get_or_404(key)
        if word.book_idf != idf:
            abort(404)
        return serialize(word), 200
    
    def delete(self, idf, key):
        word = WordModel.query.get_or_404(key)
        if word.book_idf != idf:
            abort(404)
        db.session.delete(word)
        db.session.commit()
        return {}, 204
    
    @staticmethod
    def parse_reqest():
        if Word.parser is None:
            Word.parser = reqparse.RequestParser()
            Word.parser.add_argument('abstract', type=str, location='json', required=True)
        return Word.parser.parse_args(strict=True)


def serialize(word):
    result = word.serialize()
    result['url'] = locate(word)
    result['book'] = locate_book(word.book)
    return result


def locate(word):
    return f'{locate_vocabulary(word.book)}/{word.key}'


def locate_vocabulary(book):
    return f'{locate_book(book)}/vocabulary'


def locate_book(book):
    return f'{request.url_root}api/book/{book.idf}'
