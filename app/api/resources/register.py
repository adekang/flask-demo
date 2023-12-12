import uuid
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.users import UserModel
from ..schema.register_sha import reg_args_valid
from ..common.utils import res


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        reg_args_valid(parser)
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return res(success=False, message="Repeated username!", code=400)
        else:
            try:
                data['salt'] = uuid.uuid4().hex
                hashed_password = generate_password_hash('{}{}'.format(data['salt'], data['pwd']))
                data['pwd'] = hashed_password
                user = UserModel(**data)
                user.addUser()
                return res(message="Register succeed!")
            except Exception as e:
                return res(success=False, message="Error: {}".format(e), code=500)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}