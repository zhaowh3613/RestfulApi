from flask import Blueprint
from app.libs.redprints import Redprint

# user = Blueprint('user', __name__)

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am user'

