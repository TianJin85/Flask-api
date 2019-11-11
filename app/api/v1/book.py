from flask import Blueprint
from app.libs.redprint import Redprint

# book = Blueprint('book', __name__)


api = Redprint('book')
@api.route('/get', methods=['GET'])
def get_book():
    # 不能包含动词
    # 理论是理论，
    return 'i am qiyue'

@api.route('/create', methods=['POST'])
def create_book():

    return 'create_book'