from flask import Blueprint
from app.libs.redprints import Redprint

# user = Blueprint('user', __name__)

api = Redprint('user')


# @api.route('/get')
@api.route('', methods=['GET'])
def get_user():
    return 'i am user vincent'

