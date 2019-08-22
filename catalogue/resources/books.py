from flask import request
from flask_restful import reqparse, Resource

from catalogue import database as db
from catalogue.models.books import Book as BookModel
from catalogue.models.preferences import Preference as PreferenceModel


class BookList(Resource):
    parser = None

    def get(self):
        query = BookList.parse_query()
        if query:
            query = f'%{query}%'
            books = BookModel.query.filter(BookModel.title.ilike(query, escape='/'))
        else:
            books = BookModel.query.all()
        books = [serialize(book) for book in books]
        return books, 200

    def post(self):
        body = Book.parse_reqest()
        book = BookModel(
            title=body['title'].strip(),
            author=body['author'].strip()
        )
        db.session.add(book)
        preference = PreferenceModel(book=book)
        db.session.add(preference)
        db.session.commit()
        return {'url': locate(book)}, 201
    
    @staticmethod
    def parse_query():
        if BookList.parser is None:
            BookList.parser = reqparse.RequestParser()
            BookList.parser.add_argument('query', type=str, location='args', required=False)
        query = BookList.parser.parse_args(strict=True).get('query')
        return query and query.strip()


class Book(Resource):
    parser = None

    def get(self, idf):
        book = BookModel.query.get_or_404(idf)
        return serialize(book), 200
    
    def delete(self, idf):
        book = BookModel.query.get_or_404(idf)
        db.session.delete(book)
        db.session.commit()
        return {}, 204
    
    @staticmethod
    def parse_reqest():
        if Book.parser is None:
            Book.parser = reqparse.RequestParser()
            Book.parser.add_argument('title', type=str, location='json', required=True)
            Book.parser.add_argument('author', type=str, location='json', default="")
        return Book.parser.parse_args(strict=True)


def serialize(book):
    result = book.serialize()
    result['url'] = locate(book)
    result['preference'] = locate_preference(book)
    result['vocabulary'] = locate_vocabulary(book)
    del result['idf']
    return result


def locate_vocabulary(book):
    return f'{locate(book)}/vocabulary'


def locate_preference(book):
    return f'{locate(book)}/preference'


def locate(book):
    return f'{request.url_root}api/book/{book.idf}'
