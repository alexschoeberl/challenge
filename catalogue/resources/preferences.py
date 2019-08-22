from flask import request
from flask_restful import reqparse, Resource

from catalogue import database as db
from catalogue.models.preferences import Preference as PreferenceModel


class Preference(Resource):
	parser = None

	def get(self, idf):
		preference = PreferenceModel.query.get_or_404(idf)
		return serialize(preference), 200
	
	def put(self, idf):
		preference = PreferenceModel.query.get_or_404(idf)
		body = Preference.parse_reqest()
		if 'char_min' in body:
			preference.char_min = body['char_min']
		if 'char_max' in body:
			preference.char_max = body['char_max']
		db.session.commit()
		return {'url': locate(preference)}, 200
	
	@staticmethod
	def parse_reqest():
		if Preference.parser is None:
			Preference.parser = reqparse.RequestParser()
			Preference.parser.add_argument('char_min', type=int, location='json', required=False)
			Preference.parser.add_argument('char_max', type=int, location='json', required=False)
		return Preference.parser.parse_args(strict=True)


def serialize(preference):
	result = preference.serialize()
	result['url'] = locate(preference)
	result['book'] = locate_book(preference.book)
	return result


def locate(preference):
	return f'{locate_book(preference.book)}/preference'


def locate_book(book):
	return f'{request.url_root}api/book/{book.idf}'
