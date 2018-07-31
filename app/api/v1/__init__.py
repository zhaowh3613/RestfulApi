from flask import Blueprint
from app.api.v1 import user, book


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    # user.api.register(bp_v1, url_prefix='/user')
    user.api.register(bp_v1)
    # book.api.register(bp_v1, url_prefix='/book')
    book.api.register(bp_v1)
    return bp_v1
