from flask import Flask
from flask import Blueprint
from app.libs.redprints import Redprint


# book = Blueprint('book', __name__)
api = Redprint('book')

# @book.route('/v1/book/get')
# @api.route('/v1/book/get')
@api.route('/get')
def get_book():
    return 'this is a book'

