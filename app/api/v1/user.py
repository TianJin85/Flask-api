from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import Redprint

from app.libs.token_auth import auth, User

# user = Blueprint('user', __name__)

api = Redprint('user')


class QiYue(object):
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user():
    # account secret
    # APP
    # token 是否过期 是否合法
    # token
    user = User.query.get_or_404()

    return jsonify(QiYue)


@api.route('/get', methods=['POST'])
def create_user():
    pass