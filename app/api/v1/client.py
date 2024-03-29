from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm()
    form.validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email
    }
    promise[form.type.data]()
    # 我们可以预知
    return Success()
    # switch
    # request.args.to_dict()
    # 表单 json
    # 网页 移动端
    # 注册 登录
    #  参数 校验 接受参数
    # WTForms 验证表单


def __register_user_by_email():
    form = UserEmailForm()
    form.validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)

