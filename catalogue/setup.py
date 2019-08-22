from os import getenv

from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def application():
    app = Flask('catalogue')
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # TODO: delete
    creds = f'{getenv("DBUSER")}:{getenv("DBPSSWD")}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{creds}@127.0.0.1:5432/catalogue'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/test')  # TODO: delete
    def template_test():
        return render_template('test.html')

    return app


def database(application):
    db = SQLAlchemy(application)
    return db


def interface(application):
    from catalogue.resources.books import Book, BookList
    from catalogue.resources.words import Word, WordList
    from catalogue.resources.preferences import Preference

    api = Api(application)
    api.add_resource(BookList, '/api/book')
    api.add_resource(Book, '/api/book/<int:idf>')
    api.add_resource(WordList, '/api/book/<int:idf>/vocabulary')
    api.add_resource(Word, '/api/book/<int:idf>/vocabulary/<string:key>')
    api.add_resource(Preference, '/api/book/<int:idf>/preference')

    return api
