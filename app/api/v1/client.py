from app.libs.redprints import Redprint

api = Redprint('client')


@api.route('/register')
def create_clinet():
    return 'regist client'