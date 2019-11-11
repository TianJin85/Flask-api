from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)

api = Redprint('user')
@api.route('/get')
def get_user():

    return 'i am qiyue'

@api.route('/get', methods=['POST'])
def create_user():
    pass